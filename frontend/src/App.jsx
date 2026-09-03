import React, { useEffect, useState } from "react";
import { Link, Route, Routes, useNavigate, useParams, useLocation } from "react-router-dom";
import api from "./api";

// Helper to get logged-in user
const getStoredUser = () => {
  try {
    return JSON.parse(localStorage.getItem("user") || "null");
  } catch {
    return null;
  }
};

/* ==========================================================================
   NAVBAR COMPONENT
   ========================================================================== */
function Navbar() {
  const navigate = useNavigate();
  const location = useLocation();
  const user = getStoredUser();

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/");
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link className="brand" to="/">
          <div className="brand-icon">⚡</div>
          Freelance<span>Hub</span> Pro
        </Link>

        <div className="nav-links">
          <Link 
            className={`nav-link ${location.pathname === "/projects" ? "active" : ""}`} 
            to="/projects"
          >
            Explore Projects
          </Link>
          <Link 
            className={`nav-link ${location.pathname === "/freelancers" ? "active" : ""}`} 
            to="/freelancers"
          >
            Find Talent
          </Link>
          {user && (
            <Link 
              className={`nav-link ${location.pathname === "/dashboard" ? "active" : ""}`} 
              to="/dashboard"
            >
              Dashboard
            </Link>
          )}
        </div>

        <div className="nav-actions">
          {user ? (
            <div className="nav-user">
              <div className="nav-avatar">{user.name ? user.name[0].toUpperCase() : "U"}</div>
              <div className="nav-user-info">
                <span className="nav-user-name">{user.name}</span>
                <span className="nav-user-role">{user.role}</span>
              </div>
              <button className="btn-ghost" onClick={handleLogout} title="Logout">
                Logout
              </button>
            </div>
          ) : (
            <>
              <Link className="btn-outline btn-sm" to="/login">
                Sign In
              </Link>
              <Link className="btn-primary btn-sm" to="/register">
                Join Now
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

/* ==========================================================================
   HOME / LANDING PAGE
   ========================================================================== */
function Home() {
  const navigate = useNavigate();
  const [query, setQuery] = useState("");

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      navigate(`/projects?q=${encodeURIComponent(query.trim())}`);
    } else {
      navigate("/projects");
    }
  };

  const handleQuickTag = (tag) => {
    navigate(`/projects?skill=${encodeURIComponent(tag)}`);
  };

  return (
    <>
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <div className="badge-pill">
            <span className="pulse-dot"></span>
            NEXT-GEN TALENT MARKETPLACE
          </div>

          <h1 className="hero-title">
            Hire World-Class Talent. <br />
            <span>Build Without Limits.</span>
          </h1>

          <p className="hero-desc">
            Connect with top 3% verified developers, designers, and AI specialists. 
            Post projects, evaluate realistic proposals, collaborate with milestones, and release secure escrow payments.
          </p>

          <form className="hero-search" onSubmit={handleSearchSubmit}>
            <input 
              placeholder="Search projects by skill (e.g. React, Python, AI, Web3)..." 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <button className="btn-primary" type="submit">
              Search
            </button>
          </form>

          <div className="quick-tags">
            <span>Popular:</span>
            {["React", "Python", "LangChain", "React Native", "PostgreSQL", "Figma"].map((t) => (
              <button key={t} className="quick-tag" onClick={() => handleQuickTag(t)}>
                {t}
              </button>
            ))}
          </div>

          <div className="hero-actions">
            <Link className="btn-primary" to="/projects">
              Explore Active Projects →
            </Link>
            <Link className="btn-outline" to="/freelancers">
              Browse Freelancers
            </Link>
          </div>
        </div>

        {/* Hero Showcase Glass Card */}
        <div className="hero-showcase">
          <div className="glass-card">
            <div className="showcase-header">
              <span className="showcase-eyebrow">LIVE MARKETPLACE STATUS</span>
              <span className="showcase-badge">● Active Escrow</span>
            </div>
            <h3 className="showcase-title">Featured Top Projects</h3>
            <div className="showcase-list">
              <div className="showcase-item">
                <div className="showcase-icon">⚡</div>
                <div>
                  <div style={{ fontWeight: 600, fontSize: "14px" }}>Enterprise SaaS Analytics Dashboard</div>
                  <div style={{ fontSize: "12px", color: "var(--emerald)", fontWeight: 600 }}>₹75,000 · React & WebSockets</div>
                </div>
              </div>
              <div className="showcase-item">
                <div className="showcase-icon">🩺</div>
                <div>
                  <div style={{ fontWeight: 600, fontSize: "14px" }}>Telemedicine Mobile App with Video</div>
                  <div style={{ fontSize: "12px", color: "var(--emerald)", fontWeight: 600 }}>₹1,20,000 · React Native & WebRTC</div>
                </div>
              </div>
              <div className="showcase-item">
                <div className="showcase-icon">🤖</div>
                <div>
                  <div style={{ fontWeight: 600, fontSize: "14px" }}>AI RAG Clinical Document Engine</div>
                  <div style={{ fontSize: "12px", color: "var(--emerald)", fontWeight: 600 }}>₹85,000 · Python & LangChain</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Platform Stats Bar */}
      <section className="stats-bar">
        <div className="stats-grid">
          <div className="stat-item">
            <span className="stat-number">10+</span>
            <span className="stat-label">Enterprise Projects Open</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">₹12.5M+</span>
            <span className="stat-label">Escrow Protected Payouts</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">4.95 / 5</span>
            <span className="stat-label">Average Client Rating</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">100%</span>
            <span className="stat-label">Verified Professional Talent</span>
          </div>
        </div>
      </section>

      {/* Workflow Section */}
      <section>
        <div className="section-head">
          <div className="section-eyebrow">SEAMLESS WORKFLOW</div>
          <h2 className="section-title">How FreelanceHub Pro Works</h2>
          <p className="section-desc">From initial proposal to milestone approval, experience a smooth freelance marketplace built for velocity.</p>
        </div>

        <div className="workflow-grid">
          <div className="workflow-card">
            <span className="workflow-step">STEP 01</span>
            <h3>Post & Discover</h3>
            <p>Clients create detailed project briefs with target skills and budgets. Freelancers discover tailored matches.</p>
          </div>
          <div className="workflow-card">
            <span className="workflow-step">STEP 02</span>
            <h3>Submit Proposals</h3>
            <p>Freelancers bid competitive prices with custom delivery timelines and showcase verifiable portfolios.</p>
          </div>
          <div className="workflow-card">
            <span className="workflow-step">STEP 03</span>
            <h3>Milestone Contracts</h3>
            <p>Collaborate with complete transparency. Escrow funding guarantees security for both parties.</p>
          </div>
          <div className="workflow-card">
            <span className="workflow-step">STEP 04</span>
            <h3>Release & Review</h3>
            <p>Approve deliverables, release payment milestones instantly, and build long-term platform reputation.</p>
          </div>
        </div>
      </section>
    </>
  );
}

/* ==========================================================================
   PROJECTS MARKETPLACE
   ========================================================================== */
function Projects() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState("All");
  const [filters, setFilters] = useState({
    q: "",
    skill: "",
    experience: "",
    project_type: ""
  });

  const categories = [
    { label: "All", skill: "" },
    { label: "React & Frontend", skill: "React" },
    { label: "Python & AI", skill: "Python" },
    { label: "Mobile Apps", skill: "React Native" },
    { label: "Cloud & DevOps", skill: "Kubernetes" },
    { label: "UI/UX Design", skill: "Figma" }
  ];

  const fetchProjects = async (overrideFilters = filters) => {
    setLoading(true);
    try {
      const res = await api.get("/projects", { params: overrideFilters });
      setProjects(res.data);
    } catch (err) {
      console.error("Failed to load projects:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  const handleCategorySelect = (cat) => {
    setActiveCategory(cat.label);
    const updated = { ...filters, skill: cat.skill };
    setFilters(updated);
    fetchProjects(updated);
  };

  const handleFilterSubmit = (e) => {
    e.preventDefault();
    fetchProjects();
  };

  return (
    <main className="container">
      <div className="page-header">
        <div>
          <div className="badge-pill">PROJECT MARKETPLACE</div>
          <h2 className="page-title">Explore Active Projects</h2>
          <p className="page-subtitle">Showing {projects.length} curated opportunities ready for proposals.</p>
        </div>
      </div>

      {/* Filter Panel */}
      <div className="filter-panel">
        <form className="filter-row" onSubmit={handleFilterSubmit}>
          <input 
            className="filter-input"
            placeholder="Search keywords (e.g. Dashboard, Microservice, IoT)..."
            value={filters.q}
            onChange={(e) => setFilters({ ...filters, q: e.target.value })}
          />
          <input 
            className="filter-input"
            placeholder="Required skill (e.g. React, Python)..."
            value={filters.skill}
            onChange={(e) => setFilters({ ...filters, skill: e.target.value })}
          />
          <select 
            className="filter-select"
            value={filters.experience}
            onChange={(e) => setFilters({ ...filters, experience: e.target.value })}
          >
            <option value="">All Experience</option>
            <option value="entry">Entry Level</option>
            <option value="intermediate">Intermediate</option>
            <option value="expert">Expert</option>
          </select>
          <select 
            className="filter-select"
            value={filters.project_type}
            onChange={(e) => setFilters({ ...filters, project_type: e.target.value })}
          >
            <option value="">All Types</option>
            <option value="fixed">Fixed Price</option>
            <option value="hourly">Hourly Rate</option>
          </select>
          <button className="btn-primary" type="submit">
            Filter Projects
          </button>
        </form>

        <div className="category-tabs">
          {categories.map((cat) => (
            <button
              key={cat.label}
              className={`cat-tab ${activeCategory === cat.label ? "active" : ""}`}
              onClick={() => handleCategorySelect(cat)}
            >
              {cat.label}
            </button>
          ))}
        </div>
      </div>

      {/* Projects Grid */}
      {loading ? (
        <div style={{ textAlign: "center", padding: "60px 0", color: "var(--text-muted)" }}>
          Loading active marketplace projects...
        </div>
      ) : projects.length === 0 ? (
        <div style={{ textAlign: "center", padding: "60px 0", color: "var(--text-muted)" }}>
          No projects match your current filters. Try resetting the search terms.
        </div>
      ) : (
        <div className="projects-grid">
          {projects.map((proj) => (
            <ProjectCard key={proj.id} project={proj} onProposalSubmitted={() => fetchProjects()} />
          ))}
        </div>
      )}
    </main>
  );
}

/* ==========================================================================
   PROJECT CARD & PROPOSAL DRAWER
   ========================================================================== */
function ProjectCard({ project, onProposalSubmitted }) {
  const user = getStoredUser();
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [proposalData, setProposalData] = useState({
    proposal: "",
    bid_amount: project.budget,
    estimated_days: 7
  });
  const [statusMsg, setStatusMsg] = useState("");
  const [saved, setSaved] = useState(false);

  const handleSave = async () => {
    if (!user) {
      alert("Please log in to save projects.");
      return;
    }
    try {
      await api.post(`/saved/${project.id}`);
      setSaved(true);
      setStatusMsg("Project saved to your bookmarks!");
      setTimeout(() => setStatusMsg(""), 3000);
    } catch {
      setStatusMsg("Project saved!");
    }
  };

  const handleApply = async (e) => {
    e.preventDefault();
    if (!user) {
      alert("Please sign in as a freelancer to submit proposals.");
      return;
    }
    try {
      await api.post(`/applications/project/${project.id}`, proposalData);
      setStatusMsg("Proposal submitted successfully!");
      setDrawerOpen(false);
      if (onProposalSubmitted) onProposalSubmitted();
      setTimeout(() => setStatusMsg(""), 4000);
    } catch (err) {
      setStatusMsg(err.response?.data?.error || "Failed to submit proposal.");
    }
  };

  const skillsList = project.skills ? project.skills.split(",").map((s) => s.trim()) : [];

  return (
    <article className="project-card">
      <div>
        <div className="card-top">
          <div className="card-badges">
            <span className="badge-status">{project.status || "open"}</span>
            <span className="badge-type">{project.project_type || "fixed"}</span>
          </div>
          <span style={{ fontSize: "12px", color: "var(--text-dim)" }}>
            {project.experience_level ? `Level: ${project.experience_level}` : ""}
          </span>
        </div>

        <h3 className="project-title" style={{ marginTop: "12px" }}>
          {project.title}
        </h3>

        <p className="project-desc" style={{ marginTop: "8px" }}>
          {project.description}
        </p>

        <div className="project-skills" style={{ marginTop: "14px" }}>
          {skillsList.map((skill) => (
            <span key={skill} className="skill-chip">
              {skill}
            </span>
          ))}
        </div>
      </div>

      <div>
        <div className="project-meta">
          <div className="project-budget">
            <span className="budget-label">Est. Budget</span>
            <span className="budget-val">₹{Number(project.budget).toLocaleString()}</span>
          </div>

          <div className="project-client">
            <span className="client-dot"></span>
            <span>{project.client || "Enterprise Client"}</span>
          </div>
        </div>

        {statusMsg && (
          <div className="status-alert status-success" style={{ marginTop: "10px" }}>
            {statusMsg}
          </div>
        )}

        {user && (
          <div className="card-actions" style={{ marginTop: "14px" }}>
            <button className="btn-outline btn-sm" onClick={handleSave}>
              {saved ? "★ Saved" : "☆ Save"}
            </button>
            {user.role === "freelancer" && (
              <button 
                className="btn-primary btn-sm" 
                onClick={() => setDrawerOpen(!drawerOpen)}
              >
                {drawerOpen ? "Close Drawer" : "Submit Proposal"}
              </button>
            )}
          </div>
        )}

        {drawerOpen && (
          <form className="drawer-form" onSubmit={handleApply}>
            <textarea
              required
              placeholder="Outline your approach, technical plan, and relevant experience..."
              value={proposalData.proposal}
              onChange={(e) => setProposalData({ ...proposalData, proposal: e.target.value })}
            />
            <div className="drawer-row">
              <div>
                <label style={{ fontSize: "11px", color: "var(--text-dim)" }}>Your Bid (₹)</label>
                <input
                  type="number"
                  value={proposalData.bid_amount}
                  onChange={(e) => setProposalData({ ...proposalData, bid_amount: e.target.value })}
                />
              </div>
              <div>
                <label style={{ fontSize: "11px", color: "var(--text-dim)" }}>Delivery (Days)</label>
                <input
                  type="number"
                  value={proposalData.estimated_days}
                  onChange={(e) => setProposalData({ ...proposalData, estimated_days: e.target.value })}
                />
              </div>
            </div>
            <button className="btn-primary" type="submit">
              Send Proposal
            </button>
          </form>
        )}
      </div>
    </article>
  );
}

/* ==========================================================================
   TALENT DIRECTORY (Freelancers)
   ========================================================================== */
function Freelancers() {
  const [freelancers, setFreelancers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [skillFilter, setSkillFilter] = useState("");

  const loadFreelancers = async () => {
    setLoading(true);
    try {
      const res = await api.get("/users/freelancers/search", {
        params: { q: searchTerm, skill: skillFilter }
      });
      setFreelancers(res.data);
    } catch (err) {
      console.error("Failed to load talent directory:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadFreelancers();
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    loadFreelancers();
  };

  return (
    <main className="container">
      <div className="page-header">
        <div>
          <div className="badge-pill">TALENT DIRECTORY</div>
          <h2 className="page-title">Hire Top Verified Talent</h2>
          <p className="page-subtitle">Directly review portfolios, verified client ratings, and hourly rates.</p>
        </div>
      </div>

      <div className="filter-panel">
        <form className="filter-row" style={{ gridTemplateColumns: "1.5fr 1.5fr auto" }} onSubmit={handleSearch}>
          <input 
            className="filter-input"
            placeholder="Search by freelancer name or specialty..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <input 
            className="filter-input"
            placeholder="Filter by skill (e.g. React, Python, Figma, Docker)..."
            value={skillFilter}
            onChange={(e) => setSkillFilter(e.target.value)}
          />
          <button className="btn-primary" type="submit">
            Search Talent
          </button>
        </form>
      </div>

      {loading ? (
        <div style={{ textAlign: "center", padding: "60px 0", color: "var(--text-muted)" }}>
          Loading talent directory...
        </div>
      ) : freelancers.length === 0 ? (
        <div style={{ textAlign: "center", padding: "60px 0", color: "var(--text-muted)" }}>
          No freelancers matched your criteria.
        </div>
      ) : (
        <div className="talent-grid">
          {freelancers.map((f) => {
            const skills = f.skills ? f.skills.split(",").map((s) => s.trim()) : [];
            return (
              <article key={f.id} className="talent-card">
                <div>
                  <div className="talent-top">
                    <div className="talent-avatar">
                      {f.name ? f.name[0].toUpperCase() : "F"}
                      <div className="talent-online-badge"></div>
                    </div>
                    <div className="talent-info">
                      <h3 className="talent-name">{f.name}</h3>
                      <span className="talent-location">📍 {f.location || "Available Globally"}</span>
                      <div className="talent-rating">
                        ★ {f.rating ? f.rating.toFixed(1) : "5.0"} 
                        <span style={{ color: "var(--text-dim)", fontWeight: 400 }}>
                          ({f.review_count || 0} reviews)
                        </span>
                      </div>
                    </div>
                  </div>

                  <p className="talent-bio" style={{ marginTop: "14px" }}>
                    {f.bio || "Specialized professional available for freelance contracts."}
                  </p>

                  <div className="project-skills" style={{ marginTop: "14px" }}>
                    {skills.slice(0, 4).map((s) => (
                      <span key={s} className="skill-chip">
                        {s}
                      </span>
                    ))}
                    {skills.length > 4 && (
                      <span className="skill-chip" style={{ opacity: 0.7 }}>
                        +{skills.length - 4}
                      </span>
                    )}
                  </div>
                </div>

                <div>
                  <div className="talent-meta">
                    <div className="talent-rate">
                      ₹{f.hourly_rate} <span>/ hour</span>
                    </div>
                    <span style={{ fontSize: "12px", color: "var(--text-dim)" }}>
                      {f.experience_years} yrs exp
                    </span>
                  </div>

                  <div style={{ marginTop: "14px" }}>
                    <Link className="btn-outline btn-sm" style={{ width: "100%" }} to={`/profile/${f.id}`}>
                      View Profile & Portfolios →
                    </Link>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      )}
    </main>
  );
}

/* ==========================================================================
   FREELANCER PROFILE VIEW
   ========================================================================== */
function Profile() {
  const { id } = useParams();
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get(`/users/${id}`)
      .then((res) => setProfile(res.data))
      .catch((err) => console.error("Error loading profile:", err))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) return <main className="container">Loading profile...</main>;
  if (!profile) return <main className="container">Profile not found.</main>;

  const skills = profile.skills ? profile.skills.split(",").map((s) => s.trim()) : [];

  return (
    <main className="container">
      {/* Profile Banner */}
      <div className="profile-banner">
        <div className="profile-avatar-big">
          {profile.name ? profile.name[0].toUpperCase() : "P"}
        </div>
        <div className="profile-main-info">
          <div className="badge-pill" style={{ textTransform: "uppercase" }}>
            {profile.role} · Verified
          </div>
          <h1 className="profile-name">{profile.name}</h1>
          <p className="profile-headline">{profile.bio || "Full-Stack Professional"}</p>
          
          <div className="profile-stats-row">
            <div className="profile-stat-badge">
              ⭐ {profile.rating ? profile.rating.toFixed(1) : "5.0"} ({profile.review_count || 0} reviews)
            </div>
            <div className="profile-stat-badge">
              💰 ₹{profile.hourly_rate} / hour
            </div>
            <div className="profile-stat-badge">
              💼 {profile.experience_years || 1} Years Experience
            </div>
            <div className="profile-stat-badge">
              📍 {profile.location || "Remote"}
            </div>
          </div>
        </div>
      </div>

      {/* Profile Details & Portfolio */}
      <div className="profile-content-grid">
        <div className="panel-card">
          <h3 className="panel-title">Skills & Credentials</h3>
          <div className="project-skills">
            {skills.map((s) => (
              <span key={s} className="skill-chip">
                {s}
              </span>
            ))}
          </div>

          <div style={{ marginTop: "14px", display: "flex", flexDirection: "column", gap: "10px", fontSize: "14px" }}>
            <div><strong style={{ color: "var(--text-muted)" }}>Availability:</strong> {profile.availability}</div>
            <div><strong style={{ color: "var(--text-muted)" }}>Location:</strong> {profile.location || "Remote"}</div>
          </div>
        </div>

        <div className="panel-card">
          <h3 className="panel-title">Showcase Portfolios ({profile.portfolio?.length || 0})</h3>
          {profile.portfolio && profile.portfolio.length > 0 ? (
            <div className="portfolio-grid">
              {profile.portfolio.map((port) => (
                <div key={port.id} className="portfolio-card">
                  <div>
                    <h4 className="portfolio-title">{port.title}</h4>
                    <p className="portfolio-desc" style={{ marginTop: "6px" }}>{port.description}</p>
                    <div className="project-skills" style={{ marginTop: "10px" }}>
                      {port.technologies.split(",").map((t) => (
                        <span key={t} className="skill-chip">{t.trim()}</span>
                      ))}
                    </div>
                  </div>
                  <div style={{ display: "flex", gap: "10px", marginTop: "12px" }}>
                    {port.github_url && (
                      <a className="btn-outline btn-sm" href={port.github_url} target="_blank" rel="noreferrer">
                        GitHub
                      </a>
                    )}
                    {port.live_url && (
                      <a className="btn-primary btn-sm" href={port.live_url} target="_blank" rel="noreferrer">
                        Live Demo
                      </a>
                    )}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p style={{ color: "var(--text-muted)" }}>No portfolio projects added yet.</p>
          )}
        </div>
      </div>
    </main>
  );
}

/* ==========================================================================
   DASHBOARDS (Client, Freelancer, Admin)
   ========================================================================== */
function Dashboard() {
  const user = getStoredUser();
  if (!user) return <Auth reg={false} />;

  return (
    <main className="container">
      <div className="dash-welcome">
        <div>
          <div className="badge-pill">{user.role.toUpperCase()} DASHBOARD</div>
          <h2 className="page-title" style={{ marginTop: "6px" }}>Welcome back, {user.name}</h2>
          <p className="page-subtitle">Track projects, manage proposals, and monitor milestone deliverables.</p>
        </div>
      </div>

      <NotificationsWidget />

      {user.role === "client" ? (
        <ClientDashboard />
      ) : user.role === "freelancer" ? (
        <FreelancerDashboard />
      ) : (
        <AdminDashboard />
      )}
    </main>
  );
}

function NotificationsWidget() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    api.get("/notifications")
      .then((res) => setNotes(res.data))
      .catch(() => {});
  }, []);

  return (
    <div className="notifications-panel" style={{ marginBottom: "25px" }}>
      <h3 style={{ fontSize: "16px", fontWeight: 700, marginBottom: "12px", display: "flex", alignItems: "center", gap: "8px" }}>
        🔔 Recent Notifications ({notes.length})
      </h3>
      {notes.length > 0 ? (
        <div style={{ display: "flex", flexDirection: "column" }}>
          {notes.slice(0, 5).map((n) => (
            <div key={n.id} className="note-item">
              <span className="note-title">{n.title}</span>
              <span className="note-msg">{n.message}</span>
            </div>
          ))}
        </div>
      ) : (
        <p style={{ color: "var(--text-muted)", fontSize: "13px" }}>No recent alerts.</p>
      )}
    </div>
  );
}

function ClientDashboard() {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    skills: "React, Python, MySQL",
    budget: "",
    deadline: "",
    experience_level: "intermediate",
    project_type: "fixed"
  });
  const [status, setStatus] = useState("");

  const handlePostProject = async (e) => {
    e.preventDefault();
    try {
      await api.post("/projects", formData);
      setStatus("Project published successfully!");
      setFormData({
        title: "",
        description: "",
        skills: "React, Python, MySQL",
        budget: "",
        deadline: "",
        experience_level: "intermediate",
        project_type: "fixed"
      });
      setTimeout(() => setStatus(""), 4000);
    } catch (err) {
      setStatus(err.response?.data?.error || "Failed to post project.");
    }
  };

  return (
    <div className="dash-grid">
      <form className="dash-form" onSubmit={handlePostProject}>
        <h3>Post a New Project</h3>
        <p style={{ color: "var(--text-muted)", fontSize: "13px" }}>
          Reach hundreds of verified developers and designers ready to bid on your work.
        </p>

        {status && <div className="status-alert status-success">{status}</div>}

        <input
          required
          placeholder="Project Title (e.g. Next.js SaaS Web App)"
          value={formData.title}
          onChange={(e) => setFormData({ ...formData, title: e.target.value })}
        />
        <textarea
          required
          placeholder="Project description, deliverables, and technical requirements..."
          value={formData.description}
          onChange={(e) => setFormData({ ...formData, description: e.target.value })}
        />
        <input
          placeholder="Required skills separated by comma (e.g. React, Node, AWS)"
          value={formData.skills}
          onChange={(e) => setFormData({ ...formData, skills: e.target.value })}
        />
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
          <input
            required
            type="number"
            placeholder="Budget (₹)"
            value={formData.budget}
            onChange={(e) => setFormData({ ...formData, budget: e.target.value })}
          />
          <input
            type="date"
            value={formData.deadline}
            onChange={(e) => setFormData({ ...formData, deadline: e.target.value })}
          />
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
          <select
            value={formData.experience_level}
            onChange={(e) => setFormData({ ...formData, experience_level: e.target.value })}
          >
            <option value="entry">Entry Level</option>
            <option value="intermediate">Intermediate</option>
            <option value="expert">Expert</option>
          </select>
          <select
            value={formData.project_type}
            onChange={(e) => setFormData({ ...formData, project_type: e.target.value })}
          >
            <option value="fixed">Fixed Price</option>
            <option value="hourly">Hourly Rate</option>
          </select>
        </div>
        <button className="btn-primary" type="submit" style={{ marginTop: "10px" }}>
          Publish Project to Marketplace
        </button>
      </form>

      <div className="panel-card">
        <h3 className="panel-title">Client Workflow Guide</h3>
        <div style={{ display: "flex", flexDirection: "column", gap: "14px", fontSize: "14px", color: "var(--text-muted)" }}>
          <div>
            <strong style={{ color: "#fff" }}>1. Post Clear Deliverables:</strong> State exact technical stack and milestones to attract relevant senior freelancers.
          </div>
          <div>
            <strong style={{ color: "#fff" }}>2. Review Proposals:</strong> Evaluate bids, estimated delivery schedules, and inspect live portfolio code.
          </div>
          <div>
            <strong style={{ color: "#fff" }}>3. Escrow Security:</strong> Funds are held safely in escrow and only released when you approve each deliverable.
          </div>
        </div>
      </div>
    </div>
  );
}

function FreelancerDashboard() {
  const user = getStoredUser();
  const [profile, setProfile] = useState({
    bio: "",
    skills: "",
    hourly_rate: "",
    experience_years: "",
    availability: "available",
    location: ""
  });
  const [portfolio, setPortfolio] = useState({
    title: "",
    description: "",
    technologies: "",
    github_url: "",
    live_url: ""
  });
  const [msg, setMsg] = useState("");

  useEffect(() => {
    if (user?.id) {
      api.get(`/users/${user.id}`).then((res) => {
        setProfile({
          bio: res.data.bio || "",
          skills: res.data.skills || "",
          hourly_rate: res.data.hourly_rate || "",
          experience_years: res.data.experience_years || "",
          availability: res.data.availability || "available",
          location: res.data.location || ""
        });
      });
    }
  }, [user?.id]);

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    try {
      await api.put("/users/me", profile);
      setMsg("Profile updated successfully!");
      setTimeout(() => setMsg(""), 3000);
    } catch {
      setMsg("Failed to update profile.");
    }
  };

  const handleAddPortfolio = async (e) => {
    e.preventDefault();
    try {
      await api.post("/users/portfolio", portfolio);
      setMsg("Portfolio item published!");
      setPortfolio({ title: "", description: "", technologies: "", github_url: "", live_url: "" });
      setTimeout(() => setMsg(""), 3000);
    } catch {
      setMsg("Failed to add portfolio.");
    }
  };

  return (
    <div className="dash-grid">
      <form className="dash-form" onSubmit={handleSaveProfile}>
        <h3>Update Freelancer Profile</h3>
        {msg && <div className="status-alert status-success">{msg}</div>}
        <textarea
          placeholder="Professional bio and overview..."
          value={profile.bio}
          onChange={(e) => setProfile({ ...profile, bio: e.target.value })}
        />
        <input
          placeholder="Skills (e.g. React, Python, Flask, Docker)"
          value={profile.skills}
          onChange={(e) => setProfile({ ...profile, skills: e.target.value })}
        />
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
          <input
            type="number"
            placeholder="Hourly Rate (₹)"
            value={profile.hourly_rate}
            onChange={(e) => setProfile({ ...profile, hourly_rate: e.target.value })}
          />
          <input
            type="number"
            placeholder="Years Experience"
            value={profile.experience_years}
            onChange={(e) => setProfile({ ...profile, experience_years: e.target.value })}
          />
        </div>
        <input
          placeholder="Location (e.g. Bengaluru, India)"
          value={profile.location}
          onChange={(e) => setProfile({ ...profile, location: e.target.value })}
        />
        <button className="btn-primary" type="submit">
          Save Profile Updates
        </button>
      </form>

      <form className="dash-form" onSubmit={handleAddPortfolio}>
        <h3>Add Showcase Project</h3>
        <input
          required
          placeholder="Project Title"
          value={portfolio.title}
          onChange={(e) => setPortfolio({ ...portfolio, title: e.target.value })}
        />
        <textarea
          placeholder="Brief description of the challenge and your solution..."
          value={portfolio.description}
          onChange={(e) => setPortfolio({ ...portfolio, description: e.target.value })}
        />
        <input
          placeholder="Technologies used (e.g. React, Redux, Node.js)"
          value={portfolio.technologies}
          onChange={(e) => setPortfolio({ ...portfolio, technologies: e.target.value })}
        />
        <input
          placeholder="GitHub URL"
          value={portfolio.github_url}
          onChange={(e) => setPortfolio({ ...portfolio, github_url: e.target.value })}
        />
        <input
          placeholder="Live Demo URL"
          value={portfolio.live_url}
          onChange={(e) => setPortfolio({ ...portfolio, live_url: e.target.value })}
        />
        <button className="btn-primary" type="submit">
          Add to Portfolio
        </button>
      </form>
    </div>
  );
}

function AdminDashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get("/admin/stats")
      .then((res) => setStats(res.data))
      .catch(() => {});
  }, []);

  return (
    <div className="panel-card">
      <h3 className="panel-title">Platform Operations & Metrics</h3>
      {stats ? (
        <div className="stats-grid" style={{ marginTop: "10px" }}>
          <div className="stat-item">
            <span className="stat-number">{stats.total_users || 0}</span>
            <span className="stat-label">Total Users</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">{stats.total_projects || 0}</span>
            <span className="stat-label">Active Projects</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">{stats.total_proposals || 0}</span>
            <span className="stat-label">Proposals Placed</span>
          </div>
          <div className="stat-item">
            <span className="stat-number">{stats.total_freelancers || 0}</span>
            <span className="stat-label">Verified Freelancers</span>
          </div>
        </div>
      ) : (
        <p style={{ color: "var(--text-muted)" }}>Loading platform metrics...</p>
      )}
    </div>
  );
}

/* ==========================================================================
   AUTHENTICATION (Login & Register with 1-Click Quick Demo Access)
   ========================================================================== */
function Auth({ reg = false }) {
  const navigate = useNavigate();
  const [isRegister, setIsRegister] = useState(reg);
  const [role, setRole] = useState("freelancer");
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    skills: "",
    hourly_rate: ""
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      if (isRegister) {
        await api.post("/auth/register", { ...formData, role });
        setIsRegister(false);
        setError("Account created! Please sign in below.");
      } else {
        const res = await api.post("/auth/login", {
          email: formData.email,
          password: formData.password
        });
        localStorage.setItem("token", res.data.token);
        localStorage.setItem("user", JSON.stringify(res.data.user));
        navigate("/dashboard");
      }
    } catch (err) {
      setError(err.response?.data?.error || "Authentication request failed.");
    } finally {
      setLoading(false);
    }
  };

  const fillDemo = (email, password) => {
    setFormData((prev) => ({ ...prev, email, password }));
    setIsRegister(false);
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <div className="auth-header">
          <div className="badge-pill" style={{ margin: "0 auto 10px" }}>
            FREELANCEHUB PRO
          </div>
          <h2 className="auth-title">{isRegister ? "Create an Account" : "Welcome Back"}</h2>
          <p className="auth-desc">
            {isRegister ? "Join as a client or verified talent." : "Sign in to manage projects and proposals."}
          </p>
        </div>

        {/* 1-Click Demo Login Bar */}
        {!isRegister && (
          <div className="demo-accounts">
            <span className="demo-title">⚡ Quick 1-Click Demo Logins:</span>
            <div className="demo-chips">
              <button 
                type="button" 
                className="demo-chip"
                onClick={() => fillDemo("freelancer@freelancehub.com", "free123")}
              >
                👨‍💻 Freelancer (Koushik)
              </button>
              <button 
                type="button" 
                className="demo-chip"
                onClick={() => fillDemo("client1@freelancehub.com", "client123")}
              >
                🏢 Client (NovaLabs)
              </button>
              <button 
                type="button" 
                className="demo-chip"
                onClick={() => fillDemo("admin@freelancehub.com", "admin123")}
              >
                🛡️ Admin
              </button>
            </div>
          </div>
        )}

        {error && (
          <div className="status-alert status-error">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
          {isRegister && (
            <>
              <div className="role-toggle">
                <button
                  type="button"
                  className={`role-btn ${role === "freelancer" ? "active" : ""}`}
                  onClick={() => setRole("freelancer")}
                >
                  Work as Freelancer
                </button>
                <button
                  type="button"
                  className={`role-btn ${role === "client" ? "active" : ""}`}
                  onClick={() => setRole("client")}
                >
                  Hire as Client
                </button>
              </div>

              <input
                required
                className="filter-input"
                placeholder="Full Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              />
            </>
          )}

          <input
            required
            type="email"
            className="filter-input"
            placeholder="Work Email"
            value={formData.email}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          />

          <input
            required
            type="password"
            className="filter-input"
            placeholder="Password"
            value={formData.password}
            onChange={(e) => setFormData({ ...formData, password: e.target.value })}
          />

          {isRegister && role === "freelancer" && (
            <>
              <input
                className="filter-input"
                placeholder="Core Skills (e.g. React, Python, Docker)"
                value={formData.skills}
                onChange={(e) => setFormData({ ...formData, skills: e.target.value })}
              />
              <input
                type="number"
                className="filter-input"
                placeholder="Hourly Rate ₹"
                value={formData.hourly_rate}
                onChange={(e) => setFormData({ ...formData, hourly_rate: e.target.value })}
              />
            </>
          )}

          <button className="btn-primary" type="submit" disabled={loading} style={{ marginTop: "10px" }}>
            {loading ? "Please wait..." : isRegister ? "Create Account" : "Sign In"}
          </button>
        </form>

        <div style={{ textAlign: "center", fontSize: "13px", color: "var(--text-muted)" }}>
          {isRegister ? (
            <>
              Already have an account?{" "}
              <button 
                type="button" 
                className="btn-ghost" 
                style={{ padding: "0 4px", color: "var(--primary)" }}
                onClick={() => setIsRegister(false)}
              >
                Sign In
              </button>
            </>
          ) : (
            <>
              Don't have an account?{" "}
              <button 
                type="button" 
                className="btn-ghost" 
                style={{ padding: "0 4px", color: "var(--primary)" }}
                onClick={() => setIsRegister(true)}
              >
                Join FreelanceHub
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

/* ==========================================================================
   MAIN APP ROUTER
   ========================================================================== */
export default function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Auth reg={false} />} />
        <Route path="/register" element={<Auth reg={true} />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/freelancers" element={<Freelancers />} />
        <Route path="/profile/:id" element={<Profile />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </>
  );
}
