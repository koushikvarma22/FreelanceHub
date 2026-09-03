from datetime import datetime, timezone
from .models import db, User, Portfolio, Project, Proposal, Notification

def seed_database(force=False):
    if not force and User.query.first():
        return # Database already seeded

    print("Seeding database with rich, diverse platform data...")

    # Clear existing data if forcing re-seed
    if force:
        Notification.query.delete()
        Proposal.query.delete()
        Portfolio.query.delete()
        Project.query.delete()
        User.query.delete()
        db.session.commit()

    # -------------------------------------------------------------
    # 1. ADMIN USER
    # -------------------------------------------------------------
    admin = User(
        name="System Administrator",
        email="admin@freelancehub.com",
        role="admin",
        bio="Global platform operations and trust & safety officer.",
        skills="Platform Governance, Dispute Resolution, Marketplace Analytics",
        location="San Francisco, USA",
        rating=5.0,
        review_count=52
    )
    admin.set_password("admin123")
    db.session.add(admin)

    # -------------------------------------------------------------
    # 2. CLIENT USERS
    # -------------------------------------------------------------
    client1 = User(
        name="Aarav Sharma",
        email="client1@freelancehub.com",
        role="client",
        bio="Product Director at NovaLabs. Scaling modern fintech and mobile payment ecosystems.",
        location="Bengaluru, India"
    )
    client1.set_password("client123")

    client2 = User(
        name="Elena Rostova",
        email="client2@freelancehub.com",
        role="client",
        bio="Founder & CEO at Horizon HealthTech. Building patient-first telehealth and AI diagnostics.",
        location="Singapore"
    )
    client2.set_password("client123")

    client3 = User(
        name="David Chen",
        email="david@apexretail.io",
        role="client",
        bio="Head of Engineering at Apex Commerce. Architecting high-velocity international e-commerce platforms.",
        location="San Francisco, USA"
    )
    client3.set_password("client123")

    client4 = User(
        name="Amara Okafor",
        email="amara@edupulse.org",
        role="client",
        bio="VP of Product at EduPulse Global. Creating interactive, gamified learning technologies for STEM students.",
        location="London, UK"
    )
    client4.set_password("client123")

    client5 = User(
        name="Sophia Al-Mansoor",
        email="sophia@helioclean.ae",
        role="client",
        bio="CTO at Helio Renewable Grid. Spearheading IoT clean energy monitoring and microgrid orchestration.",
        location="Dubai, UAE"
    )
    client5.set_password("client123")

    db.session.add_all([client1, client2, client3, client4, client5])

    # -------------------------------------------------------------
    # 3. FREELANCER USERS
    # -------------------------------------------------------------
    fl1 = User(
        name="Koushik Kumar",
        email="freelancer@freelancehub.com",
        role="freelancer",
        bio="Senior Full-Stack & AI Engineer with 5+ years shipping resilient React applications, Python microservices, and database optimizations.",
        skills="React, Python, Flask, MySQL, TypeScript, Docker",
        hourly_rate=1500,
        experience_years=5,
        availability="available",
        location="Hyderabad, India",
        rating=4.9,
        review_count=34
    )
    fl1.set_password("free123")

    fl2 = User(
        name="Priya Patel",
        email="priya@freelancehub.com",
        role="freelancer",
        bio="Lead UI/UX Designer & Frontend Developer crafting intuitive design systems, responsive web interfaces, and fluid micro-animations.",
        skills="React, TailwindCSS, Figma, Next.js, Framer Motion",
        hourly_rate=1200,
        experience_years=4,
        availability="available",
        location="Mumbai, India",
        rating=5.0,
        review_count=29
    )
    fl2.set_password("free123")

    fl3 = User(
        name="Marcus Vance",
        email="marcus@freelancehub.com",
        role="freelancer",
        bio="Principal Cloud & Database Architect specializing in distributed backend systems, low-latency APIs, and SQL/NoSQL scaling.",
        skills="Python, FastAPI, MySQL, PostgreSQL, AWS, Kubernetes",
        hourly_rate=2200,
        experience_years=7,
        availability="available",
        location="Berlin, Germany",
        rating=4.8,
        review_count=41
    )
    fl3.set_password("free123")

    fl4 = User(
        name="Aisha Morales",
        email="aisha@freelancehub.com",
        role="freelancer",
        bio="Specialized Mobile Developer engineering cross-platform iOS & Android applications with native performance and offline sync.",
        skills="React Native, Flutter, Swift, Kotlin, Firebase",
        hourly_rate=1800,
        experience_years=6,
        availability="available",
        location="Austin, USA",
        rating=4.9,
        review_count=23
    )
    fl4.set_password("free123")

    fl5 = User(
        name="Liam O'Connor",
        email="liam@freelancehub.com",
        role="freelancer",
        bio="DevOps & Site Reliability Specialist focused on infrastructure-as-code, zero-downtime CI/CD deployments, and cloud security.",
        skills="Terraform, Docker, Kubernetes, AWS, Prometheus, CI/CD",
        hourly_rate=2000,
        experience_years=5,
        availability="available",
        location="Dublin, Ireland",
        rating=4.9,
        review_count=18
    )
    fl5.set_password("free123")

    fl6 = User(
        name="Mei-Ling Zhou",
        email="meiling@freelancehub.com",
        role="freelancer",
        bio="Applied AI & Machine Learning Specialist developing production Retrieval-Augmented Generation (RAG) pipelines and LLM applications.",
        skills="Python, LangChain, PyTorch, OpenAI, FastAPI, VectorDB",
        hourly_rate=2500,
        experience_years=6,
        availability="available",
        location="Toronto, Canada",
        rating=5.0,
        review_count=37
    )
    fl6.set_password("free123")

    fl7 = User(
        name="Carlos Mendez",
        email="carlos@freelancehub.com",
        role="freelancer",
        bio="Blockchain Engineer & Web3 Security Researcher auditing smart contracts and creating high-performance decentralized user applications.",
        skills="Solidity, ethers.js, Web3, Next.js, Node.js, Smart Contracts",
        hourly_rate=2400,
        experience_years=5,
        availability="available",
        location="Madrid, Spain",
        rating=4.7,
        review_count=15
    )
    fl7.set_password("free123")

    fl8 = User(
        name="Samantha Reed",
        email="samantha@freelancehub.com",
        role="freelancer",
        bio="Creative Brand Director & Digital Product Strategist transforming tech startups into visually iconic and recognizable brands.",
        skills="Brand Identity, Figma, Typography, Motion Graphics, Blender",
        hourly_rate=1400,
        experience_years=4,
        availability="available",
        location="Melbourne, Australia",
        rating=4.9,
        review_count=26
    )
    fl8.set_password("free123")

    db.session.add_all([fl1, fl2, fl3, fl4, fl5, fl6, fl7, fl8])
    db.session.flush()

    # -------------------------------------------------------------
    # 4. PORTFOLIOS
    # -------------------------------------------------------------
    portfolios = [
        # Koushik Kumar
        Portfolio(
            user_id=fl1.id,
            title="Enterprise Fleet Telemetry & IoT Dashboard",
            description="Real-time vehicle tracking, route anomaly detection, and predictive maintenance portal for a fleet of 4,000+ trucks.",
            technologies="React, Flask, WebSocket, Leaflet, MySQL",
            github_url="https://github.com/example/fleet-telemetry",
            live_url="https://fleet-telemetry-demo.app"
        ),
        Portfolio(
            user_id=fl1.id,
            title="Document Intelligence & Semantic Search",
            description="Enterprise PDF search engine utilizing vector embeddings and streaming conversational answers.",
            technologies="Python, React, LangChain, FastAPI, Redis",
            github_url="https://github.com/example/doc-intelligence",
            live_url="https://docsearch-preview.app"
        ),
        # Priya Patel
        Portfolio(
            user_id=fl2.id,
            title="Fintech NeoBank Mobile UI Design System",
            description="Complete design system with 250+ accessible components, interactive states, dark mode, and design token exports.",
            technologies="Figma, React, TailwindCSS, Storybook",
            github_url="https://github.com/example/neobank-ds",
            live_url="https://neobank-design.app"
        ),
        Portfolio(
            user_id=fl2.id,
            title="SaaS Interactive Analytics Platform",
            description="Designed and coded an intuitive analytics dashboard featuring drag-and-drop widgets and custom SVG data charts.",
            technologies="React, Next.js, Framer Motion, CSS Grid",
            github_url="https://github.com/example/analytics-dash",
            live_url="https://saas-dash-preview.app"
        ),
        # Marcus Vance
        Portfolio(
            user_id=fl3.id,
            title="High-Concurrency Payments Gateway",
            description="Microservice infrastructure processing over 18,000 requests/second with distributed idempotency locks.",
            technologies="Python, FastAPI, Redis, PostgreSQL, Docker",
            github_url="https://github.com/example/fast-pay-engine",
            live_url=""
        ),
        Portfolio(
            user_id=fl3.id,
            title="Automated Multi-Tenant Database Sharding Engine",
            description="Dynamic SQL routing layer that distributes high-volume tenant transactions across geographical database clusters.",
            technologies="MySQL, Python, SQLAlchemy, Docker",
            github_url="https://github.com/example/db-sharding-layer",
            live_url=""
        ),
        # Aisha Morales
        Portfolio(
            user_id=fl4.id,
            title="PulseFit Cross-Platform Fitness App",
            description="Mobile workout companion featuring offline video caching, real-time Bluetooth heart rate monitor sync, and health metrics.",
            technologies="React Native, Redux, Firebase, Bluetooth LE",
            github_url="https://github.com/example/pulsefit-app",
            live_url="https://pulsefit.app"
        ),
        Portfolio(
            user_id=fl4.id,
            title="Artisan Coffee Roasters Delivery App",
            description="E-commerce mobile app with live order geolocation tracking, push notifications, and Apple Pay/Google Pay integration.",
            technologies="Flutter, Dart, Stripe, Google Maps API",
            github_url="https://github.com/example/artisan-coffee",
            live_url="https://artisancoffee-demo.com"
        ),
        # Liam O'Connor
        Portfolio(
            user_id=fl5.id,
            title="Automated Kubernetes GitOps Infrastructure",
            description="Production-grade cloud setup with automated blue-green releases, Prometheus alerting, and automated failover.",
            technologies="Terraform, Kubernetes, ArgoCD, AWS, Helm",
            github_url="https://github.com/example/gitops-cloud",
            live_url=""
        ),
        # Mei-Ling Zhou
        Portfolio(
            user_id=fl6.id,
            title="Financial Research RAG Synthesizer",
            description="Ingests quarterly SEC filings and company earnings call audio transcripts to generate verified investment summaries.",
            technologies="PyTorch, LangChain, OpenAI, Qdrant, FastAPI",
            github_url="https://github.com/example/finance-rag",
            live_url="https://fin-rag-synthesizer.app"
        ),
        # Carlos Mendez
        Portfolio(
            user_id=fl7.id,
            title="Decentralized Peer-to-Peer Escrow Protocol",
            description="Smart contract architecture ensuring fair milestone releases with zero intermediary fees and multi-sig arbitration.",
            technologies="Solidity, Hardhat, ethers.js, Next.js",
            github_url="https://github.com/example/escrow-protocol",
            live_url="https://escrow-web3-demo.app"
        ),
        # Samantha Reed
        Portfolio(
            user_id=fl8.id,
            title="Quantum Robotics Global Brand Identity",
            description="Brand guideline manual, 3D product renders, custom typography palette, and marketing site art direction.",
            technologies="Brand Identity, Figma, Blender, Webflow",
            github_url="https://github.com/example/quantum-branding",
            live_url="https://quantum-robotics-showcase.com"
        )
    ]
    db.session.add_all(portfolios)

    # -------------------------------------------------------------
    # 5. PROJECTS (Diverse, non-duplicate projects)
    # -------------------------------------------------------------
    projects = [
        Project(
            client_id=client1.id,
            title="Enterprise SaaS Analytics Dashboard with Real-time WebSockets",
            description="NovaLabs needs an experienced frontend engineer to build an analytics dashboard with interactive data visualizations, dark mode, responsive layout, and live WebSocket telemetry.",
            skills="React, TypeScript, Chart.js, WebSockets, TailwindCSS",
            budget=75000,
            deadline="2026-10-20",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client2.id,
            title="Cross-Platform Telemedicine Mobile App with Encrypted Video",
            description="We are building an iOS & Android app connecting certified physicians with patients. Requires secure WebRTC consultation rooms, prescription history, and push notifications.",
            skills="React Native, WebRTC, Firebase, TypeScript",
            budget=120000,
            deadline="2026-11-15",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client3.id,
            title="High-Throughput E-Commerce Inventory & Order Microservice",
            description="Apex Retail requires a backend developer to engineer an inventory synchronization service handling 50,000 SKUs across 8 regional warehouses with sub-50ms API response time.",
            skills="Python, FastAPI, PostgreSQL, Redis, Docker",
            budget=95000,
            deadline="2026-10-10",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client2.id,
            title="AI Retrieval-Augmented Generation (RAG) Clinical Document Engine",
            description="Need an applied AI specialist to build a secure RAG search pipeline that ingests medical research papers and clinical guidelines with source citations and guardrails.",
            skills="Python, LangChain, OpenAI, FastAPI, VectorDB",
            budget=85000,
            deadline="2026-10-30",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client4.id,
            title="Interactive Gamified STEM Learning Platform for High Schools",
            description="EduPulse is looking for creative frontend talent to build engaging web modules with mini-simulations, progress badges, interactive quizzes, and sound effects.",
            skills="React, Next.js, CSS Animations, Canvas, TypeScript",
            budget=65000,
            deadline="2026-11-05",
            experience_level="intermediate",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client5.id,
            title="Smart Solar Grid IoT Telemetry & Fault Detection Dashboard",
            description="Helio CleanEnergy requires a full-stack dashboard to monitor 12,000 rooftop solar panel inverters, visual heatmaps, power generation graphs, and automated outage warnings.",
            skills="React, Python, MQTT, TimescaleDB, Leaflet",
            budget=110000,
            deadline="2026-11-30",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client1.id,
            title="Biometric Non-Custodial Multi-Chain Mobile Crypto Wallet",
            description="Looking for a mobile developer with Web3 experience to implement face ID login, mnemonic seed recovery, ERC-20 / Solana token balances, and QR code transfers.",
            skills="React Native, Web3, ethers.js, TypeScript",
            budget=90000,
            deadline="2026-10-25",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client3.id,
            title="Global Multi-Cloud Kubernetes Migration & Zero-Downtime CI/CD",
            description="Architect and deploy automated Terraform infrastructure across AWS and GCP with GitOps pipeline, automated canary releases, and central log aggregation.",
            skills="Terraform, Kubernetes, AWS, GitHub Actions, Prometheus",
            budget=105000,
            deadline="2026-10-18",
            experience_level="expert",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client1.id,
            title="Complete Design System & Brand Identity Redesign for FinTech SaaS",
            description="Seeking a lead UI/UX designer to craft a unified visual language, typography scales, icon library, and Figma component system with token sync.",
            skills="Figma, Design Systems, Typography, UI/UX",
            budget=50000,
            deadline="2026-10-08",
            experience_level="intermediate",
            project_type="fixed",
            status="open"
        ),
        Project(
            client_id=client2.id,
            title="Automated Patient Appointment Scheduler with WhatsApp Reminders",
            description="Develop a Python/Flask scheduling service with calendar sync (Google/Outlook), SMS/WhatsApp reminder triggers, and patient intake forms.",
            skills="Python, Flask, REST API, Twilio, MySQL",
            budget=40000,
            deadline="2026-09-30",
            experience_level="intermediate",
            project_type="fixed",
            status="open"
        )
    ]
    db.session.add_all(projects)
    db.session.flush()

    # -------------------------------------------------------------
    # 6. PROPOSALS (Varied bids and realistic content)
    # -------------------------------------------------------------
    proposals = [
        Proposal(
            project_id=projects[0].id,
            freelancer_id=fl1.id,
            proposal="I have engineered telemetry dashboards for fleet and IoT applications handling over 10k concurrent streams. Can deliver the full React + Chart.js frontend with responsive layout and mock WebSocket server in 12 days.",
            bid_amount=70000,
            estimated_days=12,
            status="submitted"
        ),
        Proposal(
            project_id=projects[0].id,
            freelancer_id=fl2.id,
            proposal="Specialist in data visualization and micro-animations. I will design a high-contrast dark theme in Figma first, test it with your team, and build the React component library with Storybook.",
            bid_amount=75000,
            estimated_days=14,
            status="submitted"
        ),
        Proposal(
            project_id=projects[1].id,
            freelancer_id=fl4.id,
            proposal="Have built 4 production healthcare and real-time communication apps in React Native. Fully familiar with WebRTC connection negotiation, TURN/STUN relays, and HIPAA-compliant storage.",
            bid_amount=115000,
            estimated_days=21,
            status="submitted"
        ),
        Proposal(
            project_id=projects[2].id,
            freelancer_id=fl3.id,
            proposal="Backend architect with deep experience in Redis caching layers, PostgreSQL indexing strategies, and high-concurrency order placement pipelines. Can guarantee sub-40ms response times.",
            bid_amount=90000,
            estimated_days=14,
            status="submitted"
        ),
        Proposal(
            project_id=projects[3].id,
            freelancer_id=fl6.id,
            proposal="My research portfolio focuses specifically on clinical and financial RAG systems. I can implement document chunking, hybrid keyword/vector search, and factual validation checks with LangChain and Qdrant.",
            bid_amount=82000,
            estimated_days=15,
            status="submitted"
        ),
        Proposal(
            project_id=projects[7].id,
            freelancer_id=fl5.id,
            proposal="Certified AWS Solutions Architect. I have conducted multi-region Kubernetes migrations for fintechs with zero downtime. Includes automated rollback triggers and Prometheus dashboards.",
            bid_amount=100000,
            estimated_days=18,
            status="submitted"
        ),
        Proposal(
            project_id=projects[8].id,
            freelancer_id=fl8.id,
            proposal="Passionate about crafting distinct, memorable fintech identities. I will deliver brand guidelines, typography pairings, color contrast compliance matrices, and a comprehensive Figma UI kit.",
            bid_amount=48000,
            estimated_days=10,
            status="submitted"
        )
    ]
    db.session.add_all(proposals)

    # -------------------------------------------------------------
    # 7. NOTIFICATIONS
    # -------------------------------------------------------------
    notifications = [
        Notification(
            user_id=fl1.id,
            title="Welcome to FreelanceHub Pro!",
            message="Your verified profile is live. Explore curated enterprise projects and submit competitive proposals."
        ),
        Notification(
            user_id=client1.id,
            title="New Proposal Received",
            message="Koushik Kumar submitted a bid of ₹70,000 for 'Enterprise SaaS Analytics Dashboard with Real-time WebSockets'."
        ),
        Notification(
            user_id=client1.id,
            title="New Proposal Received",
            message="Priya Patel submitted a bid of ₹75,000 for 'Enterprise SaaS Analytics Dashboard with Real-time WebSockets'."
        ),
        Notification(
            user_id=client2.id,
            title="New Proposal Received",
            message="Aisha Morales submitted a bid of ₹115,000 for 'Cross-Platform Telemedicine Mobile App with Encrypted Video'."
        ),
        Notification(
            user_id=client3.id,
            title="New Proposal Received",
            message="Marcus Vance submitted a bid of ₹90,000 for 'High-Throughput E-Commerce Inventory & Order Microservice'."
        ),
        Notification(
            user_id=client2.id,
            title="New Proposal Received",
            message="Mei-Ling Zhou submitted a bid of ₹82,000 for 'AI Retrieval-Augmented Generation (RAG) Clinical Document Engine'."
        )
    ]
    db.session.add_all(notifications)

    db.session.commit()
    print("Database re-seeding completed with 8 freelancers, 5 clients, 10 projects, and 7 proposals!")
