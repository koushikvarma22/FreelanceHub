from .models import db, User, Portfolio, Project, Proposal, Notification

def seed_database():
    if User.query.first():
        return # Database already seeded

    print("Seeding database with realistic platform data...")

    # 1. Admin
    admin = User(
        name="System Administrator",
        email="admin@freelancehub.com",
        role="admin",
        bio="Platform operations and security supervisor.",
        skills="Platform Governance, Dispute Resolution, Analytics",
        rating=5.0,
        review_count=45
    )
    admin.set_password("admin123")
    db.session.add(admin)

    # 2. Clients
    client1 = User(
        name="Aarav Sharma",
        email="client1@freelancehub.com",
        role="client",
        bio="Product Director at NovaLabs. Scaling modern fintech applications.",
        location="Bengaluru, India"
    )
    client1.set_password("client123")
    db.session.add(client1)

    client2 = User(
        name="Elena Rostova",
        email="client2@freelancehub.com",
        role="client",
        bio="Founder at Horizon Health Tech. Looking for high quality React and AI developers.",
        location="Singapore"
    )
    client2.set_password("client123")
    db.session.add(client2)

    # 3. Freelancers
    fl1 = User(
        name="Koushik Kumar",
        email="freelancer@freelancehub.com",
        role="freelancer",
        bio="Senior Full-Stack & AI Engineer specializing in React, Node, Python, and scalable cloud solutions.",
        skills="React, Python, Flask, MySQL, TypeScript, Docker",
        hourly_rate=1500,
        experience_years=5,
        availability="available",
        location="Hyderabad, India",
        rating=4.9,
        review_count=28
    )
    fl1.set_password("free123")
    db.session.add(fl1)

    fl2 = User(
        name="Priya Patel",
        email="priya@freelancehub.com",
        role="freelancer",
        bio="Creative UI/UX Designer and Frontend Specialist passionate about micro-interactions and design systems.",
        skills="React, TailwindCSS, Figma, Next.js, Framer Motion",
        hourly_rate=1200,
        experience_years=4,
        availability="available",
        location="Mumbai, India",
        rating=5.0,
        review_count=19
    )
    fl2.set_password("free123")
    db.session.add(fl2)

    fl3 = User(
        name="Marcus Vance",
        email="marcus@freelancehub.com",
        role="freelancer",
        bio="Full-Stack Cloud & Database Architect with deep experience in distributed systems and performance optimization.",
        skills="Python, FastAPI, MySQL, PostgreSQL, AWS, GraphQL",
        hourly_rate=2200,
        experience_years=7,
        availability="available",
        location="Berlin, Germany",
        rating=4.8,
        review_count=34
    )
    fl3.set_password("free123")
    db.session.add(fl3)

    db.session.flush()

    # Add Portfolios
    p1 = Portfolio(
        user_id=fl1.id,
        title="Enterprise Fleet Management Dashboard",
        description="Real-time telemetry and IoT vehicle tracking dashboard with analytics and alerting.",
        technologies="React, Flask, WebSocket, MySQL, Leaflet",
        github_url="https://github.com/example/fleet-dash",
        live_url="https://fleet-dash-demo.com"
    )
    p2 = Portfolio(
        user_id=fl1.id,
        title="AI-Powered Document Summarizer",
        description="SaaS product that ingests PDFs and provides conversational question answering and summaries.",
        technologies="Python, React, LangChain, FastAPI",
        github_url="https://github.com/example/ai-doc-summary",
        live_url="https://aidocsummary.com"
    )
    p3 = Portfolio(
        user_id=fl2.id,
        title="Fintech Mobile App Design System",
        description="Comprehensive Figma component system and pixel-perfect React implementation for banking app.",
        technologies="Figma, React, TailwindCSS, Storybook",
        github_url="https://github.com/example/fintech-design",
        live_url="https://fintech-design-preview.com"
    )
    p4 = Portfolio(
        user_id=fl3.id,
        title="High-Throughput Payments Engine",
        description="Engineered transactional microservice handling 15,000 requests/sec with 99.999% uptime.",
        technologies="Python, Redis, MySQL, Docker, Kubernetes",
        github_url="https://github.com/example/payments-engine",
        live_url=""
    )
    db.session.add_all([p1, p2, p3, p4])

    # Projects
    proj1 = Project(
        client_id=client1.id,
        title="Build Modern React Dashboard for Analytics SaaS",
        description="We require a senior React developer to implement a responsive analytics dashboard with chart visualisations, dark mode, and authentication flow.",
        skills="React, TypeScript, Chart.js, REST API",
        budget=45000,
        deadline="2026-10-15",
        experience_level="intermediate",
        project_type="fixed",
        status="open"
    )
    proj2 = Project(
        client_id=client1.id,
        title="Optimize High Volume MySQL Database & API Endpoints",
        description="Our SaaS platform needs query tuning, indexing overhaul, and connection pooling optimization for MySQL 8.0.",
        skills="MySQL, Python, Database Optimization, SQLAlchemy",
        budget=35000,
        deadline="2026-09-30",
        experience_level="expert",
        project_type="fixed",
        status="open"
    )
    proj3 = Project(
        client_id=client2.id,
        title="Healthcare Patient Portal UI Implementation",
        description="Implement user-friendly frontend for telehealth platform connecting doctors with patients. Clean typography and responsive design required.",
        skills="React, CSS, Responsive Design, Accessibility",
        budget=55000,
        deadline="2026-11-01",
        experience_level="intermediate",
        project_type="fixed",
        status="open"
    )
    proj4 = Project(
        client_id=client2.id,
        title="AI Assistant Integration with Flask Backend",
        description="Connect our knowledgebase to an intelligent search API with streaming responses and secure session management.",
        skills="Python, Flask, REST API, PyJWT",
        budget=40000,
        deadline="2026-10-05",
        experience_level="expert",
        project_type="hourly",
        status="open"
    )
    db.session.add_all([proj1, proj2, proj3, proj4])
    db.session.flush()

    # Proposals
    prop1 = Proposal(
        project_id=proj1.id,
        freelancer_id=fl1.id,
        proposal="I have extensive experience building scalable React analytics portals with high fidelity charts and dark mode. Can deliver in 10 days.",
        bid_amount=42000,
        estimated_days=10,
        status="submitted"
    )
    prop2 = Proposal(
        project_id=proj2.id,
        freelancer_id=fl3.id,
        proposal="Specialist in MySQL execution plan analysis, index optimization, and SQLAlchemy connection pooling. Ready to start immediately.",
        bid_amount=35000,
        estimated_days=7,
        status="submitted"
    )
    db.session.add_all([prop1, prop2])

    # Notifications
    n1 = Notification(
        user_id=fl1.id,
        title="Welcome to FreelanceHub Pro",
        message="Your freelancer profile is active! Browse open projects and submit proposals to top clients."
    )
    n2 = Notification(
        user_id=client1.id,
        title="New proposal received",
        message="Koushik Kumar submitted a proposal for 'Build Modern React Dashboard for Analytics SaaS'."
    )
    db.session.add_all([n1, n2])

    db.session.commit()
    print("Database seeding completed successfully!")
