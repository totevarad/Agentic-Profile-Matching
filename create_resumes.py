"""
Script to generate 35 comprehensive, realistic resumes for various computer science roles
spanning latest trends (Generative AI, LLMs, MLOps, Next.js, Cloud/DevOps, Rust, Distributed Systems, etc.)
with varied experience levels (Junior 1-2y, Mid 3-5y, Senior 6-8y, Staff/Principal 9-14y).
Formats: Combination of .pdf and .docx.
"""

import os
from fpdf import FPDF
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "resumes")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 35 Candidate Specifications
CANDIDATES = [
    {
        "filename": "Alice_Smith.pdf",
        "format": "pdf",
        "name": "Alice Smith",
        "title": "Senior Python Developer & Machine Learning Engineer",
        "email": "alice.smith@devmail.io",
        "phone": "+1 (555) 234-5678",
        "location": "San Francisco, CA",
        "linkedin": "linkedin.com/in/alice-smith-ml",
        "github": "github.com/alicesmith-dev",
        "summary": "Dynamic Machine Learning Engineer and Senior Python Developer with 5+ years of experience building, evaluating, and deploying production-grade AI applications and microservices. Expert in PyTorch, scikit-learn, FastAPI, and Dockerized workflows. Proven track record in optimizing retrieval pipelines and implementing distributed ML inference engines.",
        "skills": {
            "Languages": "Python, SQL, C++, Bash",
            "Machine Learning & AI": "PyTorch, Scikit-learn, TensorFlow, HuggingFace Transformers, LangChain",
            "Backend & Frameworks": "FastAPI, Flask, Celery, REST APIs",
            "Cloud & DevOps": "Docker, Kubernetes, AWS (EC2, S3, SageMaker), Git, CI/CD",
            "Databases": "PostgreSQL, Redis, ChromaDB, Pinecone"
        },
        "experience": [
            {
                "role": "Senior Machine Learning Engineer",
                "company": "NeuralScale Innovations",
                "location": "San Francisco, CA",
                "period": "2023 - Present",
                "bullets": [
                    "Architected and deployed a multi-modal embedding retrieval pipeline using PyTorch and FastAPI, cutting inference latency by 42%.",
                    "Integrated vector similarity search with ChromaDB and Redis caching to support 15M+ daily user queries.",
                    "Designed CI/CD automation and containerized ML training jobs using Docker and Kubernetes on AWS SageMaker.",
                    "Led a squad of 4 engineers in fine-tuning open-source LLMs for industry-specific document classification."
                ]
            },
            {
                "role": "Python Backend & ML Developer",
                "company": "DataPulse Technologies",
                "location": "San Jose, CA",
                "period": "2021 - 2023",
                "bullets": [
                    "Engineered predictive analytics microservices in Python and Scikit-learn serving 250k daily active users.",
                    "Built ETL data pipelines utilizing PostgreSQL, SQLAlchemy, and Celery tasks for real-time model retraining.",
                    "Implemented comprehensive unit testing with pytest and automated linting, achieving 94% test coverage."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "University of California, Berkeley",
            "year": "2021"
        },
        "projects": [
            {
                "title": "RAG-Powered Code Search Engine",
                "tech": "Python, PyTorch, ChromaDB, FastAPI, Docker",
                "desc": "Built an intelligent semantic code search engine indexing 500k+ repositories with sub-100ms retrieval times."
            }
        ],
        "certifications": ["AWS Certified Machine Learning - Specialty", "TensorFlow Developer Certificate"]
    },
    {
        "filename": "Bob_Jones.pdf",
        "format": "pdf",
        "name": "Bob Jones",
        "title": "Mid-Level Python & Backend Developer",
        "email": "bob.jones@codecraft.org",
        "phone": "+1 (555) 345-6789",
        "location": "Austin, TX",
        "linkedin": "linkedin.com/in/bobjones-dev",
        "github": "github.com/bobjones-py",
        "summary": "Results-oriented Backend Developer with 3+ years of experience designing robust web services, RESTful APIs, and relational database schemas in Python and Django. Strong focus on database normalization, caching strategies, and code readability. Seeking to expand into enterprise cloud infrastructure and ML pipelines.",
        "skills": {
            "Languages": "Python, SQL, JavaScript, HTML/CSS",
            "Frameworks": "Django, Django REST Framework, Flask",
            "Databases": "PostgreSQL, MySQL, SQLite, Redis",
            "Tools & Practices": "Git, GitHub Actions, Pytest, Linux, Postman (Lacks extensive Cloud/AWS hands-on)"
        },
        "experience": [
            {
                "role": "Python Backend Developer",
                "company": "Apex Web Solutions",
                "location": "Austin, TX",
                "period": "2023 - Present",
                "bullets": [
                    "Developed and maintained 15+ RESTful endpoints in Django powering customer portal applications with 99.8% uptime.",
                    "Optimized complex PostgreSQL queries and added Redis caching, reducing page load times from 2.4s to 650ms.",
                    "Collaborated with frontend React developers to integrate authentication flows using JWT and OAuth2."
                ]
            },
            {
                "role": "Junior Software Developer",
                "company": "Bluefin Digital",
                "location": "Dallas, TX",
                "period": "2021 - 2023",
                "bullets": [
                    "Created automated Python scripts for database migrations and CSV report generation.",
                    "Maintained internal company tooling using Flask and SQLite, fixing 80+ software bug tickets."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Software Engineering",
            "school": "University of Texas at Dallas",
            "year": "2021"
        },
        "projects": [
            {
                "title": "Multi-Tenant Inventory API",
                "tech": "Python, Django REST Framework, PostgreSQL, Redis",
                "desc": "Architected an inventory management REST service supporting role-based access control and webhook notifications."
            }
        ],
        "certifications": ["Python Institute PCAP Certified Associate"]
    },
    {
        "filename": "Charlie_Brown.pdf",
        "format": "pdf",
        "name": "Charlie Brown",
        "title": "Junior Machine Learning Engineer",
        "email": "charlie.brown@freshgrad.io",
        "phone": "+1 (555) 456-7890",
        "location": "Boulder, CO",
        "linkedin": "linkedin.com/in/charlie-brown-ml",
        "github": "github.com/charliebrown-ai",
        "summary": "Enthusiastic Junior Machine Learning Engineer with 1+ years of experience in data preprocessing, supervised learning, and exploratory data analysis using Python, Pandas, and TensorFlow. Eager to contribute foundational ML skills while developing production containerization, Docker, and cloud deployment capabilities.",
        "skills": {
            "Languages": "Python, R, SQL, Bash",
            "Machine Learning": "TensorFlow, Keras, Scikit-learn, Pandas, NumPy, Matplotlib",
            "Tools": "Jupyter Notebooks, Git, Linux, VS Code",
            "Areas for Growth": "Docker containerization, Kubernetes orchestration, Production Cloud CI/CD"
        },
        "experience": [
            {
                "role": "Junior Data Science Associate",
                "company": "Rocky Mountain Analytics",
                "location": "Denver, CO",
                "period": "2023 - Present",
                "bullets": [
                    "Trained baseline classification and regression models using Scikit-learn and TensorFlow for customer segmentation.",
                    "Cleaned, sanitized, and transformed structured tabular datasets exceeding 2M records using Pandas and NumPy.",
                    "Prepared automated weekly Jupyter data visualization reports for senior data science stakeholders."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Data Science & Mathematics",
            "school": "University of Colorado Boulder",
            "year": "2023"
        },
        "projects": [
            {
                "title": "Customer Churn Prediction Model",
                "tech": "Python, Pandas, Scikit-learn, Matplotlib",
                "desc": "Developed a Random Forest classifier predicting subscriber churn with 83% precision on public telecom benchmarks."
            }
        ],
        "certifications": ["DeepLearning.AI Deep Learning Specialization"]
    },
    {
        "filename": "David_Chen.pdf",
        "format": "pdf",
        "name": "David Chen",
        "title": "Principal Generative AI & Systems Architect",
        "email": "david.chen@ai-architect.org",
        "phone": "+1 (555) 567-8901",
        "location": "Seattle, WA",
        "linkedin": "linkedin.com/in/davidchen-genai",
        "github": "github.com/dchen-systems",
        "summary": "Visionary AI Systems Architect with 12+ years of experience designing hyper-scale distributed computing systems, LLM inference platforms, and agentic workflows. Pioneered enterprise adoption of vLLM, TensorRT-LLM, LangGraph multi-agent orchestration, and vector search infrastructure across Kubernetes clusters on AWS and GCP.",
        "skills": {
            "Languages": "Python, C++, CUDA, Go, Rust",
            "GenAI & LLMs": "LangGraph, LangChain, vLLM, TensorRT-LLM, LlamaIndex, LoRA/QLoRA, HuggingFace",
            "Distributed Systems": "Ray, Kubernetes, Slurm, Triton Inference Server, Kafka, gRPC",
            "Cloud & Infrastructure": "AWS (EKS, SageMaker, ParallelCluster), GCP, Terraform, Docker",
            "Databases": "Milvus, Qdrant, ChromaDB, Cassandra, DynamoDB"
        },
        "experience": [
            {
                "role": "Principal AI Architect",
                "company": "Hyperion AI Systems",
                "location": "Seattle, WA",
                "period": "2020 - Present",
                "bullets": [
                    "Spearheaded enterprise LLM serving platform using vLLM and Ray on 64-node NVIDIA H100 clusters, cutting serving costs by $1.8M annually.",
                    "Designed fault-tolerant multi-agent LangGraph system coordinating automated financial research with dynamic tool invocation.",
                    "Authored company-wide technical standard for semantic caching and embedding retrieval across 50M daily transactions."
                ]
            },
            {
                "role": "Lead Distributed Systems Engineer",
                "company": "OmniCloud Networks",
                "location": "Redmond, WA",
                "period": "2016 - 2020",
                "bullets": [
                    "Engineered high-throughput distributed pub/sub infrastructure handling 800k events/sec using Go, C++, and Kafka.",
                    "Migrated monolithic backend to containerized Kubernetes microservices on AWS EKS, improving system resilience to 99.99% SLA."
                ]
            },
            {
                "role": "Senior Software Engineer",
                "company": "Pacific Software Labs",
                "location": "Bellevue, WA",
                "period": "2012 - 2016",
                "bullets": [
                    "Built low-latency C++ network proxies and asynchronous Python backend services for cloud storage platforms."
                ]
            }
        ],
        "education": {
            "degree": "M.S. in Computer Science (Distributed Systems)",
            "school": "University of Washington",
            "year": "2012"
        },
        "projects": [
            {
                "title": "OpenAgent Orchestrator",
                "tech": "Python, LangGraph, vLLM, Triton, Redis",
                "desc": "Open-source stateful agent runtime with cyclic graph execution and dynamic checkpoint recovery (4.2k GitHub stars)."
            }
        ],
        "certifications": ["AWS Certified Solutions Architect - Professional", "Kubernetes Certified Administrator (CKA)"]
    },
    {
        "filename": "Elena_Rostova.docx",
        "format": "docx",
        "name": "Elena Rostova",
        "title": "Staff MLOps & Platform Engineer",
        "email": "elena.rostova@platform-ai.net",
        "phone": "+1 (555) 678-9012",
        "location": "New York, NY",
        "linkedin": "linkedin.com/in/elena-rostova-mlops",
        "github": "github.com/erostova-ops",
        "summary": "Accomplished Staff MLOps Engineer with 9+ years of experience standardizing Machine Learning platforms, continuous delivery for AI models, and feature store architectures. Expert in Kubernetes, Kubeflow, MLflow, Terraform, and Python. Proven leader in scaling model deployment pipelines from zero to hundreds of production models.",
        "skills": {
            "Core Technologies": "Kubernetes, Docker, Python, Go, Terraform, Helm, Bash",
            "MLOps Stack": "Kubeflow, MLflow, Feast Feature Store, Seldon Core, KServe, DVC",
            "Cloud Platforms": "AWS, GCP, Azure, Hybrid On-Prem GPU clusters",
            "Monitoring & CI/CD": "Prometheus, Grafana, ArgoCD, GitHub Actions, Datadog",
            "Data & Storage": "PostgreSQL, Redis, Apache Spark, MinIO, S3"
        },
        "experience": [
            {
                "role": "Staff MLOps Engineer",
                "company": "Vanguard FinAI",
                "location": "New York, NY",
                "period": "2021 - Present",
                "bullets": [
                    "Engineered unified ML platform leveraging Kubeflow, MLflow, and Feast serving 120+ data scientists and 200+ active models.",
                    "Implemented automated canary rollouts and model drift monitoring with Prometheus and Evidently AI, reducing outage incidents by 65%.",
                    "Architected GPU cluster auto-scaling on AWS EKS with Karpenter, saving over $400k in idle GPU compute costs."
                ]
            },
            {
                "role": "Senior DevOps & Cloud Engineer",
                "company": "Metropolis Cloud Solutions",
                "location": "Jersey City, NJ",
                "period": "2017 - 2021",
                "bullets": [
                    "Authored declarative Infrastructure as Code (IaC) modules using Terraform for multi-region AWS and GCP deployments.",
                    "Established automated CI/CD pipelines with ArgoCD and Helm, driving deployment frequency from bi-weekly to 15+ times daily."
                ]
            },
            {
                "role": "Systems / Linux Engineer",
                "company": "Northeast Data Systems",
                "location": "Boston, MA",
                "period": "2015 - 2017",
                "bullets": [
                    "Maintained Linux bare-metal clusters and automated server provisioning with Ansible and Python."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Engineering",
            "school": "Columbia University",
            "year": "2015"
        },
        "projects": [
            {
                "title": "KubeDrift: Realtime Model Drift Operator",
                "tech": "Go, Kubernetes CRD, Prometheus, Python",
                "desc": "Built a Kubernetes operator that watches inference endpoints and triggers automatic retraining upon metric degradation."
            }
        ],
        "certifications": ["Certified Kubernetes Administrator (CKA)", "HashiCorp Certified Terraform Associate"]
    },
    {
        "filename": "Fatima_Al-Mansoor.pdf",
        "format": "pdf",
        "name": "Fatima Al-Mansoor",
        "title": "Senior Data Engineer",
        "email": "fatima.mansoor@datafabric.io",
        "phone": "+1 (555) 789-0123",
        "location": "Chicago, IL",
        "linkedin": "linkedin.com/in/fatima-mansoor-de",
        "github": "github.com/fatima-data",
        "summary": "Analytical Senior Data Engineer with 7+ years of experience architecting large-scale data lakehouses, streaming pipelines, and analytical data marts. Proficient in Apache Spark, Kafka, Snowflake, Databricks, dbt, and Python. Passionate about data governance, idempotency, and sub-minute analytical query latency.",
        "skills": {
            "Languages": "Python, SQL, Scala, Java, Bash",
            "Data Processing": "Apache Spark (PySpark), Apache Kafka, Apache Flink, Databricks, dbt",
            "Warehouses & Lakes": "Snowflake, Delta Lake, BigQuery, AWS Redshift",
            "Orchestration & Cloud": "Apache Airflow, Prefect, AWS (S3, EMR, Glue), Azure, Docker",
            "Storage & NoSQL": "PostgreSQL, MongoDB, Redis, Apache Iceberg"
        },
        "experience": [
            {
                "role": "Senior Data Engineer",
                "company": "Nexus Logistics Tech",
                "location": "Chicago, IL",
                "period": "2021 - Present",
                "bullets": [
                    "Designed real-time event ingestion engine processing 80k IoT telematics events/sec using Kafka and PySpark Streaming into Delta Lake.",
                    "Modernized legacy batch pipelines using dbt Core and Snowflake, decreasing nightly transformation runtimes by 3.5 hours.",
                    "Implemented comprehensive data quality checks and automated schema evolution alerts using Great Expectations and Airflow."
                ]
            },
            {
                "role": "Data Engineer",
                "company": "Midwest Financial Analytics",
                "location": "Evanston, IL",
                "period": "2017 - 2021",
                "bullets": [
                    "Built Kimball-dimensional star-schema data models in Redshift supporting enterprise executive BI dashboards.",
                    "Created automated Python Airflow DAGs for extracting financial settlement data from external REST APIs."
                ]
            }
        ],
        "education": {
            "degree": "M.S. in Information Systems & Big Data",
            "school": "Northwestern University",
            "year": "2017"
        },
        "projects": [
            {
                "title": "Lakehouse Stream Replicator",
                "tech": "Python, Kafka, Spark, Delta Lake, Docker",
                "desc": "Built an open-source zero-data-loss CDC replication utility syncing transactional Postgres databases to Delta Lake tables."
            }
        ],
        "certifications": ["Databricks Certified Data Engineer Professional", "Snowflake SnowPro Core Certified"]
    },
    {
        "filename": "George_Miller.docx",
        "format": "docx",
        "name": "George Miller",
        "title": "Full-Stack Next.js & React Architect",
        "email": "george.miller@fullstackweb.dev",
        "phone": "+1 (555) 890-1234",
        "location": "Austin, TX",
        "linkedin": "linkedin.com/in/georgemiller-dev",
        "github": "github.com/gmiller-ui",
        "summary": "Creative and technical Full-Stack Architect with 8+ years of experience engineering high-performance modern web applications with Next.js, React, TypeScript, Node.js, and GraphQL. Deep expertise in Server Actions, React Server Components (RSC), TailwindCSS, responsive design systems, and distributed backend integrations.",
        "skills": {
            "Frontend": "React, Next.js (App Router), TypeScript, JavaScript, TailwindCSS, Redux Toolkit, TanStack Query",
            "Backend": "Node.js, Express, NestJS, GraphQL, REST APIs, Python",
            "Databases": "PostgreSQL, Supabase, Prisma ORM, Redis, MongoDB",
            "DevOps & Testing": "Docker, AWS, Vercel, Jest, Playwright, Cypress, CI/CD",
            "Architecture": "Micro-frontends, Design Systems, Serverless, SSR / SSG"
        },
        "experience": [
            {
                "role": "Lead Full-Stack Architect",
                "company": "Aura Commerce Solutions",
                "location": "Austin, TX",
                "period": "2021 - Present",
                "bullets": [
                    "Architected high-volume e-commerce storefront in Next.js 14 and TypeScript handling 4M monthly pageviews with 99 Google Lighthouse score.",
                    "Constructed reusable enterprise design system with TailwindCSS and Radix UI primitives, accelerating feature development velocity across 6 squads.",
                    "Designed GraphQL federation layer in Node.js aggregating 14 microservices into a unified performant API schema."
                ]
            },
            {
                "role": "Senior Frontend / Full-Stack Engineer",
                "company": "CloudScape Interactive",
                "location": "Dallas, TX",
                "period": "2018 - 2021",
                "bullets": [
                    "Engineered interactive SaaS dashboard using React, Redux, and D3.js for visual infrastructure monitoring.",
                    "Reduced client bundle size by 54% through aggressive code-splitting, tree-shaking, and lazy route loading."
                ]
            },
            {
                "role": "Web Developer",
                "company": "PixelCraft Studios",
                "location": "Houston, TX",
                "period": "2016 - 2018",
                "bullets": [
                    "Developed responsive web applications using JavaScript, React, HTML5, CSS3, and Node.js."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "Texas A&M University",
            "year": "2016"
        },
        "projects": [
            {
                "title": "NextFlow: Headless Workflow Canvas",
                "tech": "Next.js, React, TypeScript, TailwindCSS, Prisma",
                "desc": "Built an interactive workflow graph editor featuring real-time collaborative state synchronization via WebSockets."
            }
        ],
        "certifications": ["Meta Certified Front-End Developer", "AWS Certified Developer - Associate"]
    },
    {
        "filename": "Hannah_Abbott.pdf",
        "format": "pdf",
        "name": "Hannah Abbott",
        "title": "Junior Frontend Developer",
        "email": "hannah.abbott@frontendhub.io",
        "phone": "+1 (555) 901-2345",
        "location": "Atlanta, GA",
        "linkedin": "linkedin.com/in/hannah-abbott-ui",
        "github": "github.com/hannah-codes",
        "summary": "Enthusiastic Junior Frontend Developer with 1+ years of experience crafting accessible, responsive user interfaces using React, JavaScript, HTML5, CSS3, and TailwindCSS. Detail-oriented collaborator eager to expand skills in TypeScript, Next.js, and end-to-end testing.",
        "skills": {
            "Core Technologies": "React, JavaScript (ES6+), HTML5, CSS3, TailwindCSS, Bootstrap",
            "Tools & Build": "Git, GitHub, Vite, npm/yarn, VS Code, Figma",
            "Basic Concepts": "REST APIs, State Management, Responsive Design, Web Accessibility (a11y)",
            "Currently Learning": "TypeScript, Next.js, Unit Testing with Jest"
        },
        "experience": [
            {
                "role": "Junior Frontend Developer",
                "company": "PeachTech Studios",
                "location": "Atlanta, GA",
                "period": "2023 - Present",
                "bullets": [
                    "Developed and maintained 10+ landing pages and responsive user forms using React and TailwindCSS.",
                    "Collaborated with UI/UX designers in Figma to translate wireframes into pixel-perfect web components.",
                    "Integrated third-party RESTful APIs for user verification and newsletter subscriptions."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Interactive Media & Web Development",
            "school": "Georgia Institute of Technology",
            "year": "2023"
        },
        "projects": [
            {
                "title": "RecipeFinder Web App",
                "tech": "React, JavaScript, TailwindCSS, REST API",
                "desc": "Created a responsive single-page application allowing users to search recipes with filtering by dietary constraints."
            }
        ],
        "certifications": ["freeCodeCamp Responsive Web Design & JavaScript Algorithms"]
    },
    {
        "filename": "Ibrahim_Kante.docx",
        "format": "docx",
        "name": "Ibrahim Kante",
        "title": "Lead Cloud & DevOps / SRE Engineer",
        "email": "ibrahim.kante@cloudops.net",
        "phone": "+1 (555) 012-3456",
        "location": "Philadelphia, PA",
        "linkedin": "linkedin.com/in/ibrahim-kante-sre",
        "github": "github.com/ikante-devops",
        "summary": "Visionary Lead Cloud & DevOps Engineer with 10+ years of experience directing enterprise cloud transformations, infrastructure automation, and Site Reliability Engineering practices. Specialized in Kubernetes, Terraform, AWS, Azure, Linux systems administration, and robust CI/CD automation across global multi-region footprints.",
        "skills": {
            "Cloud Providers": "AWS (Expert), Microsoft Azure, Google Cloud Platform (GCP)",
            "Containers & Orchestration": "Kubernetes (EKS/AKS), Docker, Helm, Nomad, ECS",
            "Infrastructure as Code": "Terraform, Terragrunt, Ansible, CloudFormation, Packer",
            "CI/CD & GitOps": "GitLab CI, GitHub Actions, ArgoCD, Jenkins",
            "Observability & Scripting": "Prometheus, Grafana, Datadog, ELK Stack, Python, Bash, Go"
        },
        "experience": [
            {
                "role": "Lead DevOps & SRE Engineer",
                "company": "Apex Financial Infrastructure",
                "location": "Philadelphia, PA",
                "period": "2020 - Present",
                "bullets": [
                    "Direct a distributed team of 8 DevOps and platform engineers supporting 400+ microservices on multi-region AWS EKS.",
                    "Spearheaded multi-cloud disaster recovery strategy achieving RPO < 5 mins and RTO < 15 mins across AWS and Azure.",
                    "Reduced cloud infrastructure expenditures by 38% ($1.2M annual run rate) through spot instance adoption and right-sizing automation."
                ]
            },
            {
                "role": "Senior Cloud Engineer",
                "company": "Keystone Data Systems",
                "location": "Pittsburgh, PA",
                "period": "2016 - 2020",
                "bullets": [
                    "Automated end-to-end infrastructure provisioning using Terraform and Ansible across 50+ enterprise customer VPCs.",
                    "Implemented centralized logging and distributed tracing with Elasticsearch, Fluentd, and Kibana (EFK)."
                ]
            },
            {
                "role": "Linux Systems Administrator",
                "company": "Penn Telecom Services",
                "location": "Allentown, PA",
                "period": "2014 - 2016",
                "bullets": [
                    "Managed 200+ RedHat and Ubuntu enterprise servers, configuring DNS, DHCP, firewalls, and automated Bash maintenance jobs."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Systems Networking",
            "school": "Pennsylvania State University",
            "year": "2014"
        },
        "projects": [
            {
                "title": "CloudAutoScaler Operator",
                "tech": "Go, Kubernetes, AWS SDK, Terraform",
                "desc": "Built a predictive horizontal pod and node autoscaler reacting to real-time traffic spikes before latency degradation."
            }
        ],
        "certifications": ["AWS Solutions Architect - Professional", "AWS Certified DevOps Engineer", "CKA - Certified Kubernetes Administrator"]
    },
    {
        "filename": "Julia_Zhang.pdf",
        "format": "pdf",
        "name": "Julia Zhang",
        "title": "Senior NLP & Large Language Models Engineer",
        "email": "julia.zhang@nlplabs.ai",
        "phone": "+1 (555) 123-4560",
        "location": "Boston, MA",
        "linkedin": "linkedin.com/in/juliazhang-nlp",
        "github": "github.com/jzhang-nlp",
        "summary": "Deep Learning and NLP Specialist with 6+ years of experience developing Natural Language Processing pipelines, LLM fine-tuning techniques, and semantic search systems. Master of HuggingFace Transformers, PyTorch, LangChain, LlamaIndex, and Vector Databases. Highly skilled in domain adaptation, PEFT, and hallucination reduction.",
        "skills": {
            "Languages": "Python, C++, SQL, Bash",
            "NLP & Deep Learning": "PyTorch, Transformers, HuggingFace, spaCy, NLTK, PEFT, LoRA, LangChain, LlamaIndex",
            "Vector Stores": "Pinecone, ChromaDB, Weaviate, Qdrant",
            "Backend & Infra": "FastAPI, Docker, Ray, Triton Inference Server, AWS, Git",
            "Techniques": "RAG, Guardrails, Instruction Tuning, Prompt Engineering, Embedding Distillation"
        },
        "experience": [
            {
                "role": "Senior NLP Engineer",
                "company": "CognitiveSearch AI",
                "location": "Boston, MA",
                "period": "2021 - Present",
                "bullets": [
                    "Built enterprise RAG architecture combining hybrid dense-sparse retrieval (BM25 + Cohere reranker) with sub-150ms latency.",
                    "Fine-tuned Llama-3 8B models using QLoRA for medical record summarization, increasing factual accuracy score from 71% to 94%.",
                    "Deployed model inference servers via Triton Inference Server and FastAPI on AWS EC2 G5 GPU instances."
                ]
            },
            {
                "role": "NLP Research Engineer",
                "company": "LexiSemantic Labs",
                "location": "Cambridge, MA",
                "period": "2018 - 2021",
                "bullets": [
                    "Trained domain-specific BERT and RoBERTa models for multi-lingual legal document classification in PyTorch.",
                    "Published 2 peer-reviewed papers on named-entity recognition in low-resource specialized domains."
                ]
            }
        ],
        "education": {
            "degree": "M.S. in Computational Linguistics",
            "school": "Harvard University",
            "year": "2018"
        },
        "projects": [
            {
                "title": "TruthCheck: Hallucination Detection Engine",
                "tech": "Python, PyTorch, Transformers, FastAPI",
                "desc": "Built an automated hallucination verification library comparing LLM outputs against source knowledge bases."
            }
        ],
        "certifications": ["Stanford Online Natural Language Processing with Deep Learning", "AWS Machine Learning Specialty"]
    },
    {
        "filename": "Kevin_Patel.docx",
        "format": "docx",
        "name": "Kevin Patel",
        "title": "Mid-Level Cybersecurity & DevSecOps Engineer",
        "email": "kevin.patel@cyberdefense.sec",
        "phone": "+1 (555) 234-5671",
        "location": "Raleigh, NC",
        "linkedin": "linkedin.com/in/kevinpatel-sec",
        "github": "github.com/kpatel-sec",
        "summary": "Proactive DevSecOps and Information Security Engineer with 4+ years of experience integrating security controls into CI/CD pipelines, container runtime defenses, and threat modeling frameworks. Proficient in Python, Linux, Docker security scanning, Kubernetes network policies, SIEM, and AWS cloud posture management.",
        "skills": {
            "Security Domains": "DevSecOps, Application Security, Threat Modeling, Vulnerability Management, Zero Trust",
            "Tools & Scanners": "Trivy, Snyk, SonarQube, OWASP ZAP, Falco, Splunk, Wazuh",
            "Cloud & DevOps": "AWS, Docker, Kubernetes, Linux, Terraform, GitHub Actions, GitLab CI",
            "Languages & Scripting": "Python, Bash, Go, SQL"
        },
        "experience": [
            {
                "role": "DevSecOps Engineer",
                "company": "SecureCloud Dynamics",
                "location": "Raleigh, NC",
                "period": "2022 - Present",
                "bullets": [
                    "Integrated automated static (SAST) and software composition analysis (SCA) with Snyk and SonarQube in CI/CD pipelines.",
                    "Configured Falco runtime container anomaly detection across 30+ Kubernetes production clusters.",
                    "Performed threat modeling workshops with engineering teams, resolving 140+ critical CVE vulnerabilities."
                ]
            },
            {
                "role": "Security Operations Center (SOC) Analyst",
                "company": "Triangle Cyber Defense",
                "location": "Durham, NC",
                "period": "2020 - 2022",
                "bullets": [
                    "Monitored Splunk SIEM alerts, investigated suspicious incident indicators, and triaged phishing campaigns.",
                    "Wrote automated Python and Bash scripts to extract forensic artifact indicators from Linux endpoints."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Cybersecurity & Information Assurance",
            "school": "North Carolina State University",
            "year": "2020"
        },
        "projects": [
            {
                "title": "KubeGuard: Automated RBAC Auditor",
                "tech": "Python, Kubernetes API, Docker, Bash",
                "desc": "Built an automated scanner detecting over-privileged service accounts and insecure Kubernetes pod specifications."
            }
        ],
        "certifications": ["CompTIA Security+", "Certified Kubernetes Security Specialist (CKS)", "AWS Certified Security - Specialty"]
    },
    {
        "filename": "Laura_Vance.pdf",
        "format": "pdf",
        "name": "Laura Vance",
        "title": "Staff Computer Vision & Spatial Computing Engineer",
        "email": "laura.vance@visioncore.ai",
        "phone": "+1 (555) 345-6782",
        "location": "Sunnyvale, CA",
        "linkedin": "linkedin.com/in/lauravance-vision",
        "github": "github.com/lvance-cv",
        "summary": "Accomplished Computer Vision Specialist and Staff Engineer with 11+ years of experience architecting real-time perception stacks, 3D spatial reconstruction, and neural rendering engines. Expert in C++, Python, PyTorch, OpenCV, CUDA, TensorRT, and state-of-the-art vision models (YOLO, Segment Anything, NeRF, 3D Gaussian Splatting).",
        "skills": {
            "Languages": "C++, Python, CUDA, Rust",
            "Vision & AI": "OpenCV, PyTorch, TensorRT, YOLOv8/v9, Segment Anything (SAM), NeRF, Point Cloud Library (PCL)",
            "Frameworks": "ROS/ROS2, OpenGL, WebGPU, Triton, ONNX",
            "Systems & Tools": "Linux, Docker, Git, NVIDIA Jetson, Edge TPUs, CMake"
        },
        "experience": [
            {
                "role": "Staff Computer Vision Engineer",
                "company": "SpatialSense Robotics",
                "location": "Sunnyvale, CA",
                "period": "2019 - Present",
                "bullets": [
                    "Architected edge perception pipeline processing 4K multi-camera 60 FPS feeds using C++, CUDA, and TensorRT on NVIDIA Jetson Orin.",
                    "Trained custom vision-language models for zero-shot object defect segmentation, delivering 99.4% precision in factory automation.",
                    "Led team of 7 computer vision researchers in developing 3D spatial reconstruction utilizing neural radiance fields (NeRF)."
                ]
            },
            {
                "role": "Senior Computer Vision Engineer",
                "company": "OpticWave Systems",
                "location": "San Jose, CA",
                "period": "2015 - 2019",
                "bullets": [
                    "Developed multi-target visual tracking algorithms and stereo depth estimation pipelines using OpenCV and C++.",
                    "Optimized deep neural network inference on embedded edge chips using quantization and pruning (INT8/FP16)."
                ]
            },
            {
                "role": "Computer Vision Software Engineer",
                "company": "VisualEdge Labs",
                "location": "Santa Clara, CA",
                "period": "2013 - 2015",
                "bullets": [
                    "Implemented feature detection, visual odometry, and image stitching algorithms for aerial drone photography."
                ]
            }
        ],
        "education": {
            "degree": "Ph.D. in Computer Science (Computer Vision & Robotics)",
            "school": "Stanford University",
            "year": "2013"
        },
        "projects": [
            {
                "title": "FastSplat: Real-Time 3D Gaussian Splatting Renderer",
                "tech": "C++, CUDA, PyTorch, WebGPU",
                "desc": "High-performance real-time 3D scene reconstruction engine rendering complex environments at 120 FPS."
            }
        ],
        "certifications": ["NVIDIA Deep Learning Institute Certified in Edge AI", "Certified Computer Vision Professional"]
    },
    {
        "filename": "Marcus_Thorne.docx",
        "format": "docx",
        "name": "Marcus Thorne",
        "title": "Senior Distributed Systems & Go Backend Engineer",
        "email": "marcus.thorne@distribsys.dev",
        "phone": "+1 (555) 456-7893",
        "location": "Portland, OR",
        "linkedin": "linkedin.com/in/marcus-thorne-go",
        "github": "github.com/mthorne-backend",
        "summary": "Technical Senior Backend Engineer with 7+ years of experience engineering fault-tolerant distributed systems, low-latency microservices, and asynchronous event meshes using Go (Golang), Python, gRPC, and Apache Kafka. Passionate about Raft consensus, concurrent systems, and high-throughput database design.",
        "skills": {
            "Languages": "Go (Golang), Python, C++, SQL, Bash",
            "Distributed Protocols": "gRPC, Protocol Buffers, Apache Kafka, NATS, WebSockets, REST",
            "Databases & Caching": "PostgreSQL, CockroachDB, Redis, Cassandra, DynamoDB",
            "Infrastructure": "Docker, Kubernetes, AWS, Linux, Terraform, Prometheus, Jaeger Tracing"
        },
        "experience": [
            {
                "role": "Senior Distributed Systems Engineer",
                "company": "Kinetix Streaming Platforms",
                "location": "Portland, OR",
                "period": "2021 - Present",
                "bullets": [
                    "Designed Go microservices engine handling 500k concurrent WebSocket connections and 40k financial ticker events/sec.",
                    "Migrated database tier from monolithic PostgreSQL to distributed CockroachDB with zero downtime and multi-region resilience.",
                    "Implemented distributed tracing with OpenTelemetry and Jaeger, identifying cross-service bottlenecks and cutting p99 latency by 50%."
                ]
            },
            {
                "role": "Backend Software Engineer",
                "company": "Cascade Cloud Services",
                "location": "Eugene, OR",
                "period": "2017 - 2021",
                "bullets": [
                    "Created high-throughput asynchronous background processing jobs in Go and Python backed by Redis Streams.",
                    "Built secure REST and gRPC API layers for internal developer infrastructure provisioning."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "Oregon State University",
            "year": "2017"
        },
        "projects": [
            {
                "title": "MiniRaft: Distributed Consensus Engine",
                "tech": "Go, gRPC, Protobuf, Docker",
                "desc": "Built an educational Raft implementation featuring dynamic leader election, log replication, and automated cluster recovery."
            }
        ],
        "certifications": ["CKAD - Certified Kubernetes Application Developer", "Go Advanced Concurrency & Systems Specialist"]
    },
    {
        "filename": "Nina_Kowalski.pdf",
        "format": "pdf",
        "name": "Nina Kowalski",
        "title": "Senior Autonomous Systems & Robotics Engineer",
        "email": "nina.kowalski@autonomylabs.tech",
        "phone": "+1 (555) 567-8904",
        "location": "Pittsburgh, PA",
        "linkedin": "linkedin.com/in/nina-kowalski-robotics",
        "github": "github.com/nkowalski-robotics",
        "summary": "Robotics Software Engineer with 6+ years of experience creating perception, localization (SLAM), and motion planning pipelines for autonomous mobile robots. Highly skilled in C++, ROS2, Python, Linux, LiDAR processing, and state estimation (Kalman filters). Experienced in hardware-in-the-loop simulation.",
        "skills": {
            "Languages": "C++, Python, Bash, MATLAB",
            "Robotics & Autonomy": "ROS/ROS2, MoveIt2, Nav2, Cartographer SLAM, Point Cloud Library (PCL), Gazebo, Isaac Sim",
            "Algorithms": "Extended Kalman Filter (EKF), Particle Filters, A*, RRT*, Model Predictive Control (MPC)",
            "Hardware & Protocols": "CAN bus, Serial, LiDAR, Stereo Cameras, IMU, Jetson AGX Orin, Linux RT"
        },
        "experience": [
            {
                "role": "Senior Robotics Software Engineer",
                "company": "Vanguard Autonomous Fleet",
                "location": "Pittsburgh, PA",
                "period": "2021 - Present",
                "bullets": [
                    "Engineered 3D LiDAR and visual-inertial SLAM pipeline using ROS2 and C++ for automated warehouse tugger robots.",
                    "Implemented real-time obstacle avoidance and dynamic path replanning utilizing Model Predictive Control (MPC).",
                    "Built automated CI simulation testing suite in NVIDIA Isaac Sim and Docker, testing 200+ edge navigation scenarios daily."
                ]
            },
            {
                "role": "Robotics Controls Engineer",
                "company": "SteelCity Automation",
                "location": "Pittsburgh, PA",
                "period": "2018 - 2021",
                "bullets": [
                    "Developed low-level embedded motor controllers and safety interlocks for industrial robotic arms.",
                    "Wrote Python data collection and telemetry visualization tools for field deployment debugging."
                ]
            }
        ],
        "education": {
            "degree": "M.S. in Robotics Engineering",
            "school": "Carnegie Mellon University",
            "year": "2018"
        },
        "projects": [
            {
                "title": "Nav2 Custom Costmap Plugin",
                "tech": "C++, ROS2, PCL, Linux",
                "desc": "Built an open-source ROS2 costmap layer for dynamic obstacle tracking and velocity prediction in unstructured spaces."
            }
        ],
        "certifications": ["ROS2 Industrial Developer Certified", "NVIDIA Jetson AI Specialist"]
    },
    {
        "filename": "Omar_Farooq.docx",
        "format": "docx",
        "name": "Omar Farooq",
        "title": "Senior Blockchain & Smart Contracts Engineer",
        "email": "omar.farooq@web3core.eth",
        "phone": "+1 (555) 678-9015",
        "location": "Miami, FL",
        "linkedin": "linkedin.com/in/omar-farooq-web3",
        "github": "github.com/omar-solidity",
        "summary": "Seasoned Web3 Engineer with 5+ years of experience authoring, testing, and securing smart contracts across Ethereum, Polygon, and Arbitrum. Master of Solidity, Rust, Hardhat, Foundry, and Web3.js. Proven track record in auditing decentralized protocols and managing multi-million-dollar liquidity pools.",
        "skills": {
            "Languages": "Solidity, Rust, TypeScript, JavaScript, Python, Go",
            "Web3 Tech": "EVM, Hardhat, Foundry, Ethers.js, Web3.js, The Graph, IPFS",
            "Standards & Protocols": "ERC-20, ERC-721, ERC-1155, DeFi AMMs, Staking, Account Abstraction (ERC-4337)",
            "Backend & DevOps": "Node.js, PostgreSQL, Docker, Git, CI/CD"
        },
        "experience": [
            {
                "role": "Senior Smart Contract Engineer",
                "company": "Aether DeFi Labs",
                "location": "Miami, FL",
                "period": "2022 - Present",
                "bullets": [
                    "Architected audited decentralized lending protocol in Solidity handling $45M Total Value Locked (TVL) without security breaches.",
                    "Wrote automated fuzz testing suites using Foundry, achieving 98% state transition branch coverage.",
                    "Integrated subgraphs using The Graph protocol for ultra-fast frontend indexing of on-chain trading events."
                ]
            },
            {
                "role": "Blockchain Developer",
                "company": "BlockForge Technologies",
                "location": "Fort Lauderdale, FL",
                "period": "2020 - 2022",
                "bullets": [
                    "Created dynamic NFT minting contracts (ERC-721A) with optimized gas usage, reducing mint gas fees by 68%.",
                    "Built backend indexing microservices in TypeScript and Node.js watching EVM block confirmations."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science & Cryptography",
            "school": "University of Miami",
            "year": "2020"
        },
        "projects": [
            {
                "title": "ZeroFee Gasless Paymaster",
                "tech": "Solidity, ERC-4337, TypeScript, Ethers.js",
                "desc": "Built an account abstraction paymaster allowing decentralized application users to transact without native gas tokens."
            }
        ],
        "certifications": ["ConsenSys Certified Blockchain Developer", "Certified Ethereum Smart Contract Auditor"]
    },
    {
        "filename": "Priya_Sharma.pdf",
        "format": "pdf",
        "name": "Priya Sharma",
        "title": "Lead Data Scientist & Analytics Specialist",
        "email": "priya.sharma@predictiveai.io",
        "phone": "+1 (555) 789-0126",
        "location": "Jersey City, NJ",
        "linkedin": "linkedin.com/in/priya-sharma-ds",
        "github": "github.com/psharma-analytics",
        "summary": "Strategic and mathematically grounded Lead Data Scientist with 8+ years of experience leading cross-functional teams in predictive modeling, statistical inference, customer lifetime value optimization, and deep learning algorithms. Proficient in Python, R, SQL, PyTorch, Scikit-learn, Tableau, and AWS cloud analytics.",
        "skills": {
            "Languages": "Python, R, SQL, SAS",
            "Machine Learning": "Scikit-learn, XGBoost, LightGBM, PyTorch, Statsmodels, SciPy",
            "Analytics & BI": "Tableau, Power BI, Looker, A/B Testing, Multivariate Analysis, Causal Inference",
            "Data & Cloud": "Pandas, NumPy, Snowflake, BigQuery, AWS (SageMaker, S3, Redshift), Spark",
            "Leadership": "Agile Data Science, Stakeholder Management, Mentorship"
        },
        "experience": [
            {
                "role": "Lead Data Scientist",
                "company": "Equitas FinTech Solutions",
                "location": "New York, NY",
                "period": "2021 - Present",
                "bullets": [
                    "Direct a team of 6 data scientists developing fraud detection and real-time credit scoring models generating $3.2M in annual loss prevention.",
                    "Designed rigorous A/B testing experimentation framework evaluating 50+ product experiments with strict false-positive controls.",
                    "Collaborated with executive leadership to translate complex algorithmic outputs into strategic product roadmaps."
                ]
            },
            {
                "role": "Senior Data Scientist",
                "company": "OmniRetail Global",
                "location": "Hoboken, NJ",
                "period": "2018 - 2021",
                "bullets": [
                    "Built customer churn and dynamic pricing recommendation models using XGBoost and PySpark on Databricks.",
                    "Constructed automated Tableau executive dashboards tracking predictive KPI metrics for 12 business units."
                ]
            },
            {
                "role": "Data Analyst",
                "company": "Metro Health Analytics",
                "location": "Newark, NJ",
                "period": "2016 - 2018",
                "bullets": [
                    "Performed cohort retention studies, SQL database mining, and clinical trial statistical analysis."
                ]
            }
        ],
        "education": {
            "degree": "M.S. in Applied Statistics & Machine Learning",
            "school": "Columbia University",
            "year": "2016"
        },
        "projects": [
            {
                "title": "CausalML Experimentation Toolkit",
                "tech": "Python, Statsmodels, Scikit-learn, Streamlit",
                "desc": "Built an internal causal inference package estimating treatment effects under confounding observational data."
            }
        ],
        "certifications": ["AWS Certified Machine Learning - Specialty", "INFORMS Certified Analytics Professional (CAP)"]
    },
    {
        "filename": "Quentin_Blake.docx",
        "format": "docx",
        "name": "Quentin Blake",
        "title": "Mid-Level Mobile App Developer - React Native & iOS",
        "email": "quentin.blake@mobileforge.dev",
        "phone": "+1 (555) 890-1237",
        "location": "Denver, CO",
        "linkedin": "linkedin.com/in/quentin-blake-mobile",
        "github": "github.com/qblake-apps",
        "summary": "Dynamic Mobile Application Developer with 3+ years of experience engineering cross-platform iOS and Android applications in React Native, TypeScript, and native Swift. Deep understanding of mobile performance profiling, offline-first synchronization, native bridge modules, and automated App Store releases.",
        "skills": {
            "Mobile Technologies": "React Native, Expo, TypeScript, JavaScript, Swift (iOS), Kotlin (Android basic)",
            "State & Storage": "Redux Toolkit, Zustand, WatermelonDB, SQLite, AsyncStorage",
            "Backend Integration": "REST APIs, GraphQL, Firebase, WebSockets, Supabase",
            "Tools & Release": "Xcode, Android Studio, Fastlane, Git, Jest, App Store Connect, Google Play Console"
        },
        "experience": [
            {
                "role": "React Native Mobile Developer",
                "company": "Summit Health Tech",
                "location": "Denver, CO",
                "period": "2023 - Present",
                "bullets": [
                    "Developed patient health tracking app in React Native and TypeScript maintaining 4.8-star rating across 150k active downloads.",
                    "Implemented offline-first SQLite database synchronization enabling seamless appointment tracking without cellular reception.",
                    "Created automated Fastlane pipelines for automated code signing, beta TestFlight distribution, and Play Store publishing."
                ]
            },
            {
                "role": "Junior Mobile Developer",
                "company": "MileHigh Apps",
                "location": "Boulder, CO",
                "period": "2021 - 2023",
                "bullets": [
                    "Built 20+ responsive mobile UI screens in React Native following Figma design specifications.",
                    "Integrated push notifications with Firebase Cloud Messaging (FCM) and Apple APNs."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "University of Colorado",
            "year": "2021"
        },
        "projects": [
            {
                "title": "FitSync: Cross-Platform Workout Tracker",
                "tech": "React Native, TypeScript, Zustand, HealthKit",
                "desc": "Built an interactive workout tracker app syncing biometrics directly with Apple HealthKit and Google Fit."
            }
        ],
        "certifications": ["Meta React Native Certified Professional"]
    },
    {
        "filename": "Rachel_Green.pdf",
        "format": "pdf",
        "name": "Rachel Green",
        "title": "Senior QA Automation & SDET Lead",
        "email": "rachel.green@testcraft.io",
        "phone": "+1 (555) 901-2348",
        "location": "Minneapolis, MN",
        "linkedin": "linkedin.com/in/rachel-green-qa",
        "github": "github.com/rgreen-sdet",
        "summary": "Quality Engineering Leader with 7+ years of experience developing robust end-to-end automation frameworks, performance testing suites, and continuous testing gates. Expert in Playwright, Cypress, Selenium, Python, TypeScript, and Dockerized test runners. Committed to zero-defect deployments and shift-left testing methodologies.",
        "skills": {
            "Automation Frameworks": "Playwright, Cypress, Selenium WebDriver, Pytest, Appium, Jest, k6",
            "Languages": "TypeScript, Python, JavaScript, Java, Bash, SQL",
            "CI/CD & DevOps": "GitHub Actions, GitLab CI, Docker, Kubernetes, Jenkins, Allure Reporting",
            "Testing Domains": "E2E Testing, API Testing, Performance Testing, Regression, Security Smoke Testing"
        },
        "experience": [
            {
                "role": "Lead SDET / QA Automation Engineer",
                "company": "NorthStar SaaS Systems",
                "location": "Minneapolis, MN",
                "period": "2021 - Present",
                "bullets": [
                    "Architected company-wide Playwright and TypeScript end-to-end test framework cutting regression cycle from 18 hours to 25 minutes.",
                    "Integrated parallelized Dockerized test executions into GitHub Actions running 3,500+ test scenarios on every pull request.",
                    "Conducted performance and stress testing with k6, uncovering memory leaks prior to major Black Friday traffic surges."
                ]
            },
            {
                "role": "QA Automation Engineer",
                "company": "TwinCities Financial Tech",
                "location": "St. Paul, MN",
                "period": "2017 - 2021",
                "bullets": [
                    "Automated 400+ REST API test cases in Python using Pytest and Requests with dynamic token generation.",
                    "Collaborated with product managers to write BDD Gherkin user acceptance criteria in Cucumber."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Software Engineering",
            "school": "University of Minnesota",
            "year": "2017"
        },
        "projects": [
            {
                "title": "AutoFlake: Flaky Test Analyzer",
                "tech": "TypeScript, Playwright, Node.js, GitHub Actions",
                "desc": "Built an automated GitHub bot that detects and isolates intermittent flaky tests before pipeline failure."
            }
        ],
        "certifications": ["ISTQB Advanced Level Test Automation Engineer", "Certified Playwright Automation Specialist"]
    },
    {
        "filename": "Samuel_OConnor.docx",
        "format": "docx",
        "name": "Samuel O'Connor",
        "title": "Staff Site Reliability Engineer (SRE)",
        "email": "samuel.oconnor@reliability.org",
        "phone": "+1 (555) 012-3459",
        "location": "San Francisco, CA",
        "linkedin": "linkedin.com/in/samuel-oconnor-sre",
        "github": "github.com/soconnor-sre",
        "summary": "Pragmatic Staff Site Reliability Engineer with 10+ years of experience engineering high-availability cloud platforms, incident response protocols, and chaos engineering experiments. Specialized in Linux kernel performance tuning, Kubernetes, Go, Python, Prometheus, Grafana, and SLA/SLO definition for tier-1 services.",
        "skills": {
            "Platforms & Infra": "Linux (Debian/RHEL/Ubuntu), Kubernetes, Docker, AWS, GCP, Terraform",
            "Languages": "Go, Python, Bash, C",
            "Observability": "Prometheus, Grafana, Cortex, Thanos, OpenTelemetry, Datadog, Vector",
            "SRE Practices": "SLIs/SLOs, Error Budgets, Chaos Engineering (Chaos Mesh), Post-Mortem Facilitation, Disaster Recovery"
        },
        "experience": [
            {
                "role": "Staff SRE",
                "company": "CloudWave Systems",
                "location": "San Francisco, CA",
                "period": "2020 - Present",
                "bullets": [
                    "Defended 99.995% uptime across 1,200 Kubernetes production nodes processing $10B+ in annual transaction volume.",
                    "Created automated remediation bots in Go that resolve 45% of tier-1 alerting pages without human intervention.",
                    "Instituted chaos engineering game days simulating network partitions and datacenter power outages with Chaos Mesh."
                ]
            },
            {
                "role": "Senior Infrastructure & SRE Engineer",
                "company": "BayPoint Media Services",
                "location": "Oakland, CA",
                "period": "2016 - 2020",
                "bullets": [
                    "Implemented unified global observability stack using Prometheus, Thanos, and Grafana across multi-region deployments.",
                    "Wrote automated Python scripts for kernel parameter optimization (sysctl) on edge caching Nginx proxy instances."
                ]
            },
            {
                "role": "Systems Administrator",
                "company": "Pacific Coast Networks",
                "location": "San Francisco, CA",
                "period": "2014 - 2016",
                "bullets": [
                    "Maintained DNS, load balancers, and Linux server fleet, responding to on-call operational escalations."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "San Francisco State University",
            "year": "2014"
        },
        "projects": [
            {
                "title": "AlertDeduper: Intelligent Incident Grouper",
                "tech": "Go, Prometheus Alertmanager API, Slack Webhooks",
                "desc": "Built an intelligent incident deduplicator that collapsed alert storms by 82% during cascading outages."
            }
        ],
        "certifications": ["Linux Foundation Certified Engineer (LFCE)", "Certified Kubernetes Administrator (CKA)"]
    },
    {
        "filename": "Tanya_Ivanova.pdf",
        "format": "pdf",
        "name": "Tanya Ivanova",
        "title": "Senior Rust & Systems Performance Engineer",
        "email": "tanya.ivanova@lowlatency.tech",
        "phone": "+1 (555) 123-4562",
        "location": "Seattle, WA",
        "linkedin": "linkedin.com/in/tanya-ivanova-rust",
        "github": "github.com/tivanova-systems",
        "summary": "Systems Programmer and Performance Engineer with 6+ years of experience building memory-safe, ultra-low-latency backend infrastructure and networking engines using Rust, C++, and WebAssembly. Skilled in Tokio asynchronous runtime, zero-copy deserialization, multi-threading, and Linux perf profiling.",
        "skills": {
            "Languages": "Rust, C++, C, WebAssembly (Wasm), Python, Bash",
            "Rust Ecosystem": "Tokio, Actix-web, Axum, Serde, Rayon, Nom, Tonic (gRPC)",
            "Systems & Tools": "Linux, eBPF, Valgrind, GDB, Perf, Flamegraphs, Docker, Git",
            "Networking": "TCP/UDP sockets, QUIC, WebSockets, ZeroMQ, Low-latency Ring Buffers"
        },
        "experience": [
            {
                "role": "Senior Rust Engineer",
                "company": "ZeroCopy Networks",
                "location": "Seattle, WA",
                "period": "2021 - Present",
                "bullets": [
                    "Authored high-frequency packet processing engine in Rust with sub-10 microsecond latency and zero heap allocations.",
                    "Engineered asynchronous gRPC microservices handling 2M requests/sec using Tokio and Tonic with minimal CPU footprint.",
                    "Profiled and eliminated cache-miss hotspots using Linux perf and custom flamegraph diagnostics."
                ]
            },
            {
                "role": "Systems Software Developer",
                "company": "Cascade High-Performance Computing",
                "location": "Bellevue, WA",
                "period": "2018 - 2021",
                "bullets": [
                    "Ported legacy C++ multithreaded simulation libraries to Rust, eliminating concurrency race conditions.",
                    "Constructed WebAssembly runtime sandbox for executing untrusted user-submitted mathematical scripts."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Engineering",
            "school": "University of Washington",
            "year": "2018"
        },
        "projects": [
            {
                "title": "FastQueue: Lock-Free SPMC Ring Buffer",
                "tech": "Rust, Atomix, Criterion Benchmarking",
                "desc": "Built an open-source lock-free single-producer multi-consumer queue achieving 80M ops/sec on consumer hardware."
            }
        ],
        "certifications": ["Linux Foundation Systems Programming Specialist"]
    },
    {
        "filename": "Umair_Siddiqui.docx",
        "format": "docx",
        "name": "Umair Siddiqui",
        "title": "Mid-Level Cloud Solutions Architect",
        "email": "umair.siddiqui@cloudarch.io",
        "phone": "+1 (555) 234-5673",
        "location": "Dallas, TX",
        "linkedin": "linkedin.com/in/umair-siddiqui-cloud",
        "github": "github.com/usiddiqui-cloud",
        "summary": "Customer-facing Cloud Solutions Architect and Consultant with 4+ years of experience designing secure, scalable multi-tier architectures on AWS and Azure. Proficient in Terraform, Python, Docker, Kubernetes, and enterprise microservices migration. Passionate about Well-Architected Framework reviews and cloud cost optimization.",
        "skills": {
            "Cloud Platforms": "AWS (EC2, S3, RDS, Lambda, ECS, CloudFront), Microsoft Azure",
            "Infrastructure as Code": "Terraform, AWS CloudFormation, Bicep, Ansible",
            "Containers & Backend": "Docker, Kubernetes, Python, Node.js, REST APIs",
            "Competencies": "Well-Architected Reviews, Disaster Recovery, Cost Optimization, Security Compliance"
        },
        "experience": [
            {
                "role": "Cloud Solutions Architect",
                "company": "Stratus Enterprise Consulting",
                "location": "Dallas, TX",
                "period": "2022 - Present",
                "bullets": [
                    "Architected and led the cloud migration of 12 enterprise clients from on-premises datacenters to AWS, reducing downtime to near zero.",
                    "Automated multi-account landing zones using AWS Organizations and Terraform, enforcing strict compliance guardrails.",
                    "Conducted AWS Well-Architected reviews for clients, identifying average compute cost savings of 30%."
                ]
            },
            {
                "role": "Cloud Support & Systems Engineer",
                "company": "LoneStar Cloud Systems",
                "location": "Plano, TX",
                "period": "2020 - 2022",
                "bullets": [
                    "Diagnosed and resolved complex AWS networking issues involving VPC Peering, Transit Gateway, and Direct Connect.",
                    "Wrote automated Python Lambda functions for automated daily EBS volume snapshot rotation."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Information Technology & Networking",
            "school": "University of Texas at Arlington",
            "year": "2020"
        },
        "projects": [
            {
                "title": "Multi-Region VPC Peering Automation",
                "tech": "Terraform, AWS VPC, Python, Git",
                "desc": "Created open-source Terraform module automating cross-region Transit Gateway routing and route table updates."
            }
        ],
        "certifications": ["AWS Certified Solutions Architect - Associate", "AWS Certified SysOps Administrator", "HashiCorp Terraform Associate"]
    },
    {
        "filename": "Valerie_Dupuis.pdf",
        "format": "pdf",
        "name": "Valerie Dupuis",
        "title": "Junior Full-Stack Developer",
        "email": "valerie.dupuis@webcraft.ca",
        "phone": "+1 (555) 345-6784",
        "location": "Montreal, QC",
        "linkedin": "linkedin.com/in/valerie-dupuis-dev",
        "github": "github.com/vdupuis-fullstack",
        "summary": "Motivated Junior Full-Stack Developer with 2+ years of experience building dynamic web applications with React, Node.js, Express, JavaScript, and MongoDB. Strong eye for clean component design and responsive CSS layouts. Enthusiastic about TypeScript and modern serverless backends.",
        "skills": {
            "Frontend": "React, JavaScript (ES6+), HTML5, CSS3, TailwindCSS, Redux",
            "Backend": "Node.js, Express, REST APIs, MongoDB, Mongoose, PostgreSQL",
            "Tools": "Git, GitHub, Postman, npm, Docker basic, VS Code"
        },
        "experience": [
            {
                "role": "Junior Full-Stack Developer",
                "company": "Quebec Digital Media",
                "location": "Montreal, QC",
                "period": "2022 - Present",
                "bullets": [
                    "Built 15+ interactive React user components and connected them to Node.js / Express REST backends.",
                    "Implemented user authorization and session management using JWT and bcrypt in MongoDB.",
                    "Participated in daily agile standups and delivered bug fixes across the full application stack."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Software Development",
            "school": "McGill University",
            "year": "2022"
        },
        "projects": [
            {
                "title": "TaskMaster Collaborative Board",
                "tech": "React, Node.js, Express, MongoDB, Socket.io",
                "desc": "Built real-time Kanban board application featuring drag-and-drop task movement and instant socket updates."
            }
        ],
        "certifications": ["Full Stack Open Certification (University of Helsinki)"]
    },
    {
        "filename": "William_Vance.docx",
        "format": "docx",
        "name": "William Vance",
        "title": "Principal Database & Distributed Storage Architect",
        "email": "william.vance@dbarchitects.com",
        "phone": "+1 (555) 456-7895",
        "location": "Austin, TX",
        "linkedin": "linkedin.com/in/william-vance-data",
        "github": "github.com/wvance-databases",
        "summary": "Master Database Architect with 14+ years of experience leading database reliability, distributed storage engines, and high-volume transaction processing systems. Deep technical authority in PostgreSQL internals, Apache Cassandra, Redis, database partitioning, ACID transactions, and zero-downtime schema evolution.",
        "skills": {
            "Relational & Distributed DBs": "PostgreSQL, CockroachDB, MySQL, Apache Cassandra, ScyllaDB, Spanner",
            "In-Memory & NoSQL": "Redis, DynamoDB, MongoDB, Memcached",
            "Systems & Tools": "Linux kernel I/O tuning, pg_bouncer, Patroni, Docker, Kubernetes, Python, C",
            "Architecture": "Replication, Sharding, WAL Archiving, CDC, High Availability, Disaster Recovery"
        },
        "experience": [
            {
                "role": "Principal Database Architect",
                "company": "Global FinPay Networks",
                "location": "Austin, TX",
                "period": "2018 - Present",
                "bullets": [
                    "Architected globally distributed PostgreSQL active-passive failover topology using Patroni and Consul, ensuring zero data loss (RPO=0).",
                    "Optimized database indexing and vacuum strategies for 80TB transactional cluster, reducing peak write latency by 65%.",
                    "Designed Cassandra time-series audit cluster handling 1.2M writes/sec with predictable p99 < 8ms."
                ]
            },
            {
                "role": "Lead Database Administrator",
                "company": "Texas Cloud Storage Systems",
                "location": "San Antonio, TX",
                "period": "2014 - 2018",
                "bullets": [
                    "Engineered automated backup and PITR recovery validation routines across 200+ enterprise customer databases.",
                    "Authored company handbook on SQL query performance tuning, caching strategies, and connection pool sizing."
                ]
            },
            {
                "role": "Senior Database Engineer",
                "company": "Austin Technology Solutions",
                "location": "Austin, TX",
                "period": "2010 - 2014",
                "bullets": [
                    "Administered mission-critical MySQL and Oracle databases, performing migrations, patching, and replication setups."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "University of Texas at Austin",
            "year": "2010"
        },
        "projects": [
            {
                "title": "PgTuneAutomator",
                "tech": "Python, PostgreSQL internals, Linux sysfs",
                "desc": "Built an automated daemon dynamically tuning PostgreSQL shared_buffers and work_mem based on live hardware utilization."
            }
        ],
        "certifications": ["EnterpriseDB Certified PostgreSQL Associate & Professional", "Cassandra Certified Architect"]
    },
    {
        "filename": "Xavier_Mendoza.pdf",
        "format": "pdf",
        "name": "Xavier Mendoza",
        "title": "Senior AI Agent & RAG Systems Engineer",
        "email": "xavier.mendoza@agentic-systems.ai",
        "phone": "+1 (555) 567-8906",
        "location": "San Jose, CA",
        "linkedin": "linkedin.com/in/xaviermendoza-ai",
        "github": "github.com/xmendoza-agents",
        "summary": "Innovative AI Software Engineer with 5+ years of experience designing Agentic Workflows, LangGraph state machines, advanced RAG architectures, and tool-augmented LLM applications. Proficient in Python, LangChain, LlamaIndex, ChromaDB, FastAPI, Docker, and PyTorch. Expert in structured schema output extraction and automated evaluation.",
        "skills": {
            "Languages": "Python, TypeScript, SQL, Bash",
            "Agentic AI & LLMs": "LangGraph, LangChain, LlamaIndex, OpenAI API, Anthropic Claude, HuggingFace, DSPy",
            "Vector Stores": "ChromaDB, Pinecone, Qdrant, Milvus, pgvector",
            "Backend & Infra": "FastAPI, Docker, Redis, Celery, AWS, Git, CI/CD",
            "Techniques": "ReAct agents, Plan-and-Solve, Self-Correction loops, Function Calling, Semantic Routing"
        },
        "experience": [
            {
                "role": "Senior Agentic AI Engineer",
                "company": "Synthetix Agent Labs",
                "location": "San Jose, CA",
                "period": "2023 - Present",
                "bullets": [
                    "Architected multi-agent customer support triage pipeline in LangGraph featuring human-in-the-loop escalation gates.",
                    "Designed advanced RAG pipeline incorporating recursive text chunking and re-ranking, boosting retrieval precision by 38%.",
                    "Integrated automated LLM-as-a-judge regression evaluation suites with Ragas, decreasing hallucination incidents to < 2%."
                ]
            },
            {
                "role": "Python Backend & AI Developer",
                "company": "Silicon Valley Software Works",
                "location": "Palo Alto, CA",
                "period": "2021 - 2023",
                "bullets": [
                    "Engineered asynchronous FastAPI microservices exposing embedding and summarization APIs to web frontends.",
                    "Containerized local LLM development environments with Docker Compose and ChromaDB vector persistence."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science & Artificial Intelligence",
            "school": "San Jose State University",
            "year": "2021"
        },
        "projects": [
            {
                "title": "Agentic Resume Screener",
                "tech": "Python, LangGraph, LangChain, ChromaDB, Gradio",
                "desc": "Built an intelligent multi-round candidate screening agent with dynamic requirement refinement and comparison tools."
            }
        ],
        "certifications": ["LangChain Certified Application Developer", "DeepLearning.AI LangGraph Specialist"]
    },
    {
        "filename": "Yuki_Tanaka.docx",
        "format": "docx",
        "name": "Yuki Tanaka",
        "title": "Senior Quantum Computing & HPC Algorithm Specialist",
        "email": "yuki.tanaka@quantumscale.tech",
        "phone": "+1 (555) 678-9017",
        "location": "Boulder, CO",
        "linkedin": "linkedin.com/in/yuki-tanaka-quantum",
        "github": "github.com/ytanaka-hpc",
        "summary": "Computational Scientist and HPC Engineer with 7+ years of experience researching quantum algorithms, numerical linear algebra, and GPU-accelerated computing. Proficient in Python, C++, CUDA, Qiskit, Cirq, OpenMP, and Slurm workload scheduling. Specializes in quantum circuit optimization and variational quantum eigensolvers (VQE).",
        "skills": {
            "Quantum SDKs": "Qiskit, Cirq, Pennylane, Q-CTRL, QuTiP",
            "HPC & Acceleration": "CUDA, OpenMP, MPI, Slurm, C++, Python (NumPy, SciPy)",
            "Mathematics": "Quantum Information Theory, Linear Algebra, Hamiltonian Simulation, Optimization",
            "Tools": "Linux, Git, CMake, Docker"
        },
        "experience": [
            {
                "role": "Senior Quantum Software Engineer",
                "company": "Aether Quantum Systems",
                "location": "Boulder, CO",
                "period": "2021 - Present",
                "bullets": [
                    "Developed hybrid quantum-classical algorithms (VQE/QAOA) in Qiskit for molecular ground state energy estimation.",
                    "Engineered GPU-accelerated quantum circuit simulator using C++ and CUDA, achieving 18x speedup over CPU baselines.",
                    "Authored transpiler optimization passes reducing two-qubit CNOT gate depth by 32% on noisy intermediate-scale quantum (NISQ) devices."
                ]
            },
            {
                "role": "HPC Research Associate",
                "company": "National Computational Labs",
                "location": "Golden, CO",
                "period": "2017 - 2021",
                "bullets": [
                    "Implemented parallelized numerical PDE solvers using C++, MPI, and OpenMP across 2,048 cluster cores.",
                    "Profiled memory bandwidth bottlenecks in large matrix decomposition kernels."
                ]
            }
        ],
        "education": {
            "degree": "Ph.D. in Applied Physics & Computational Science",
            "school": "University of Colorado",
            "year": "2017"
        },
        "projects": [
            {
                "title": "CuQSim: CUDA Quantum State Vector Simulator",
                "tech": "CUDA, C++, Python, Qiskit C-extensions",
                "desc": "Built a 32-qubit GPU state vector simulator with multi-GPU tensor contraction support."
            }
        ],
        "certifications": ["IBM Certified Quantum Developer - Quantum Computation with Qiskit"]
    },
    {
        "filename": "Zara_Khan.pdf",
        "format": "pdf",
        "name": "Zara Khan",
        "title": "Junior Data Analyst & BI Developer",
        "email": "zara.khan@analyticsbridge.io",
        "phone": "+1 (555) 789-0128",
        "location": "Houston, TX",
        "linkedin": "linkedin.com/in/zara-khan-bi",
        "github": "github.com/zkhan-data",
        "summary": "Detail-oriented Junior Data Analyst with 1+ years of experience extracting business insights, creating automated dashboards, and writing clean SQL queries. Proficient in SQL, Python, Pandas, Tableau, and Microsoft Excel. Eager to grow data engineering skills in cloud databases and ETL automation.",
        "skills": {
            "Languages": "SQL, Python, Bash basic",
            "Data & BI Tools": "Tableau, Power BI, Excel (Advanced formulas, Power Query), Pandas, NumPy",
            "Databases": "PostgreSQL, MySQL, Snowflake basic",
            "Techniques": "Exploratory Data Analysis (EDA), Cohort Analysis, KPI Reporting, Data Cleaning"
        },
        "experience": [
            {
                "role": "Junior Data Analyst",
                "company": "Gulf Coast Energy Insights",
                "location": "Houston, TX",
                "period": "2023 - Present",
                "bullets": [
                    "Wrote complex SQL queries with CTEs and window functions to aggregate daily refinery production metrics.",
                    "Designed 5 interactive Tableau dashboards adopted by operations managers for real-time asset tracking.",
                    "Automated weekly manual data scrubbing workflows in Python using Pandas, saving 6 hours per week."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Management Information Systems",
            "school": "University of Houston",
            "year": "2023"
        },
        "projects": [
            {
                "title": "E-Commerce Customer Retention Dashboard",
                "tech": "SQL, Tableau, Python, Pandas",
                "desc": "Built an end-to-end cohort retention analysis calculating churn rate and customer lifetime value on 500k orders."
            }
        ],
        "certifications": ["Tableau Desktop Specialist", "Google Data Analytics Professional Certificate"]
    },
    {
        "filename": "Alexander_Wright.docx",
        "format": "docx",
        "name": "Alexander Wright",
        "title": "Senior Microservices & API Platform Engineer",
        "email": "alexander.wright@apipoint.net",
        "phone": "+1 (555) 890-1239",
        "location": "Columbus, OH",
        "linkedin": "linkedin.com/in/alexander-wright-java",
        "github": "github.com/awright-platform",
        "summary": "Enterprise Software Engineer with 6+ years of experience architecting event-driven microservices architectures, distributed API gateways, and asynchronous messaging backbones using Java, Spring Boot, Apache Kafka, and Kubernetes. Passionate about domain-driven design, high concurrency, and resilient cloud services.",
        "skills": {
            "Languages": "Java (17/21), Kotlin, SQL, Python, Bash",
            "Frameworks": "Spring Boot, Spring Cloud, Quarkus, Hibernate/JPA",
            "Event & Messaging": "Apache Kafka, RabbitMQ, gRPC, REST",
            "Cloud & Infra": "Docker, Kubernetes, AWS, PostgreSQL, Redis, Maven, Gradle"
        },
        "experience": [
            {
                "role": "Senior Microservices Engineer",
                "company": "Midwest Insurance Group",
                "location": "Columbus, OH",
                "period": "2021 - Present",
                "bullets": [
                    "Architected claims processing event mesh using Java 17, Spring Boot, and Kafka handling 20M events daily.",
                    "Implemented resilient circuit-breaker and retry patterns with Resilience4j across 25 integrated microservices.",
                    "Mentored junior engineers on Domain-Driven Design (DDD) aggregates and clean hex architecture."
                ]
            },
            {
                "role": "Java Software Engineer",
                "company": "Buckeye State Software",
                "location": "Cincinnati, OH",
                "period": "2018 - 2021",
                "bullets": [
                    "Developed backend RESTful APIs with Spring Boot and PostgreSQL supporting customer mobile banking applications.",
                    "Wrote comprehensive unit and integration tests using JUnit 5, Mockito, and Testcontainers."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "Ohio State University",
            "year": "2018"
        },
        "projects": [
            {
                "title": "EventMesh Starter Kit",
                "tech": "Java, Spring Boot, Kafka, Testcontainers",
                "desc": "Built an open-source template for idempotent Kafka consumer services with transactional outbox pattern."
            }
        ],
        "certifications": ["Oracle Certified Professional: Java SE 17 Developer", "Confluent Certified Developer for Apache Kafka"]
    },
    {
        "filename": "Beatrice_Gomez.pdf",
        "format": "pdf",
        "name": "Beatrice Gomez",
        "title": "Mid-Level Edge AI & Embedded Systems Engineer",
        "email": "beatrice.gomez@edgetech.io",
        "phone": "+1 (555) 901-2340",
        "location": "Phoenix, AZ",
        "linkedin": "linkedin.com/in/beatrice-gomez-edge",
        "github": "github.com/bgomez-embedded",
        "summary": "Specialized Embedded Software Engineer with 4+ years of experience optimizing deep learning models for resource-constrained microcontrollers and edge processors. Master of C++, Python, Embedded Linux, TensorFlow Lite, ONNX, and ARM Cortex architectures. Experienced in sensor fusion and power-constrained inference.",
        "skills": {
            "Languages": "C, C++, Python, Assembly (ARM), Bash",
            "Edge AI": "TensorFlow Lite Micro, ONNX Runtime, OpenVINO, Edge Impulse, PyTorch",
            "Embedded Systems": "Embedded Linux, FreeRTOS, Yocto Project, STM32, ESP32, Raspberry Pi, Jetson Nano",
            "Protocols": "I2C, SPI, UART, CAN, BLE, MQTT"
        },
        "experience": [
            {
                "role": "Embedded AI Engineer",
                "company": "SensorScale IoT",
                "location": "Phoenix, AZ",
                "period": "2022 - Present",
                "bullets": [
                    "Quantized and deployed audio keyword spotting neural networks onto ARM Cortex-M4 consuming under 15mW power.",
                    "Built custom Yocto Linux image for gateway devices integrating camera feeds and local ONNX model inference.",
                    "Created automated Python hardware-in-the-loop (HIL) test harness executing on firmware flashing."
                ]
            },
            {
                "role": "Junior Embedded Firmware Engineer",
                "company": "Desert Micro Instruments",
                "location": "Tempe, AZ",
                "period": "2020 - 2022",
                "bullets": [
                    "Wrote peripheral device drivers in C for environmental sensors communicating via I2C and SPI.",
                    "Debugged timing jitter and interrupt priorities using logic analyzers and oscilloscopes."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Electrical & Computer Engineering",
            "school": "Arizona State University",
            "year": "2020"
        },
        "projects": [
            {
                "title": "TinyVibration: Anomaly Detector",
                "tech": "C++, TFLite Micro, FreeRTOS, STM32",
                "desc": "Built an ultra-low-power vibration anomaly detector predicting mechanical motor bearing failures."
            }
        ],
        "certifications": ["Arm Accredited Engineer (AAE)", "Embedded Linux Development with Yocto"]
    },
    {
        "filename": "Carlos_Reyes.docx",
        "format": "docx",
        "name": "Carlos Reyes",
        "title": "Staff Platform & Internal Developer Experience Engineer",
        "email": "carlos.reyes@platformeng.dev",
        "phone": "+1 (555) 012-3451",
        "location": "San Antonio, TX",
        "linkedin": "linkedin.com/in/carlos-reyes-platform",
        "github": "github.com/creyes-platform",
        "summary": "Impact-driven Staff Platform Engineer with 9+ years of experience building Internal Developer Platforms (IDP), self-service developer tooling, and automated GitOps delivery pipelines. Expert in Kubernetes, Go, Backstage, ArgoCD, Terraform, and cloud-native standards. Dedicated to reducing cognitive load for hundreds of software engineers.",
        "skills": {
            "Core Technologies": "Kubernetes, Go, Backstage (Spotify), Terraform, Helm, Docker, Linux",
            "GitOps & CI/CD": "ArgoCD, GitHub Actions, Crossplane, Tekton",
            "Cloud & Observability": "AWS, GCP, Prometheus, Datadog, OpenTelemetry",
            "Practices": "Platform-as-a-Product, Golden Paths, Self-Service Infrastructure, Developer Productivity"
        },
        "experience": [
            {
                "role": "Staff Platform Engineer",
                "company": "Alamo Tech Group",
                "location": "San Antonio, TX",
                "period": "2021 - Present",
                "bullets": [
                    "Created internal developer portal using Spotify Backstage adopted by 350+ engineers, cutting new service provisioning from 3 weeks to 10 minutes.",
                    "Engineered Kubernetes custom controllers in Go and Crossplane to provide self-service AWS S3 buckets and RDS databases.",
                    "Standardized GitOps workflows across 80 microservices with ArgoCD, driving deployment failure rate down from 12% to under 0.8%."
                ]
            },
            {
                "role": "Senior Cloud Infrastructure Engineer",
                "company": "Austin Cyber Cloud",
                "location": "Austin, TX",
                "period": "2017 - 2021",
                "bullets": [
                    "Provisioned immutable infrastructure with Terraform across multiple enterprise AWS regions.",
                    "Wrote automated container security admission controllers using Open Policy Agent (OPA) Gatekeeper."
                ]
            },
            {
                "role": "DevOps Engineer",
                "company": "Texas Software Labs",
                "location": "San Antonio, TX",
                "period": "2015 - 2017",
                "bullets": [
                    "Built Jenkins continuous integration jobs and automated testing triggers for monolithic codebases."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science",
            "school": "University of Texas at San Antonio",
            "year": "2015"
        },
        "projects": [
            {
                "title": "KubeScaffold: Service Generator CLI",
                "tech": "Go, Cobra, Helm, Backstage Plugin",
                "desc": "Built a CLI generating production-ready microservices with Dockerfile, Helm charts, and CI/CD pipelines in one command."
            }
        ],
        "certifications": ["Certified Kubernetes Administrator (CKA)", "HashiCorp Certified Terraform Associate"]
    },
    {
        "filename": "Diana_Prince.pdf",
        "format": "pdf",
        "name": "Diana Prince",
        "title": "Senior FinTech Backend & Low Latency Engineer",
        "email": "diana.prince@finengine.com",
        "phone": "+1 (555) 123-4563",
        "location": "New York, NY",
        "linkedin": "linkedin.com/in/diana-prince-fintech",
        "github": "github.com/dprince-trading",
        "summary": "High-caliber Backend Systems Engineer with 8+ years of experience engineering mission-critical financial trading engines, order routing systems, and market data feeds. Deep proficiency in Java, C++, Apache Kafka, distributed consensus, FIX protocol, and microsecond latency optimization under heavy volatility.",
        "skills": {
            "Languages": "Java (Low-GC, Aeron, Disruptor), C++, SQL, Python",
            "FinTech Systems": "FIX Protocol, Market Data Feeds, Order Book Matching, Algorithmic Execution",
            "Messaging & Data": "Apache Kafka, LMAX Disruptor, Aeron, Chronicle Queue, Redis, PostgreSQL",
            "Infrastructure": "Linux low-latency kernel tuning, Docker, Git, Prometheus"
        },
        "experience": [
            {
                "role": "Senior Low-Latency Backend Engineer",
                "company": "Manhattan Quant Trading",
                "location": "New York, NY",
                "period": "2020 - Present",
                "bullets": [
                    "Engineered algorithmic order execution engine in Java using LMAX Disruptor processing 85k messages/sec at sub-50 microsecond latency.",
                    "Integrated real-time market data multicast parser supporting CME and NASDAQ direct feeds.",
                    "Tuned JVM garbage collection (ZGC) and off-heap memory buffers, eliminating stop-the-world latency spikes."
                ]
            },
            {
                "role": "FinTech Software Engineer",
                "company": "WallStreet Financial Tech",
                "location": "Jersey City, NJ",
                "period": "2016 - 2020",
                "bullets": [
                    "Developed settlement and reconciliation microservices using Spring Boot, Kafka, and PostgreSQL.",
                    "Implemented FIX protocol compliant client gateway for institutional broker connectivity."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Science & Financial Engineering",
            "school": "New York University",
            "year": "2016"
        },
        "projects": [
            {
                "title": "MicroBook: High-Performance Limit Order Book",
                "tech": "Java 21, LMAX Disruptor, Off-Heap Memory",
                "desc": "Built an ultra-fast in-memory limit order book handling 100k limit orders/sec with deterministic matching latency."
            }
        ],
        "certifications": ["Oracle Certified Professional: Java Developer", "Financial Markets Regulatory & Technology Certification"]
    },
    {
        "filename": "Ethan_Hunt.docx",
        "format": "docx",
        "name": "Ethan Hunt",
        "title": "Senior Threat Intelligence & Penetration Testing Specialist",
        "email": "ethan.hunt@redteamlabs.sec",
        "phone": "+1 (555) 234-5674",
        "location": "Washington, DC",
        "linkedin": "linkedin.com/in/ethan-hunt-infosec",
        "github": "github.com/ehunt-redteam",
        "summary": "Elite Offensive Security Consultant and Red Team Operator with 7+ years of experience conducting advanced adversary simulations, cloud penetration tests, and vulnerability research. Proficient in Python, Linux, Metasploit, Cobalt Strike, Burp Suite, Active Directory exploitation, and AWS IAM privilege escalation.",
        "skills": {
            "Offensive Security": "Red Teaming, Penetration Testing, Active Directory Exploitation, Web App Pentesting (OWASP Top 10)",
            "Tools": "Burp Suite Pro, Metasploit, BloodHound, Cobalt Strike, Wireshark, Nmap, Ghidra",
            "Cloud Security": "AWS Security, Azure AD Pentesting, Pacu, CloudSploit, ScoutSuite",
            "Languages & Scripting": "Python, Bash, PowerShell, C, Assembly x86 basic"
        },
        "experience": [
            {
                "role": "Senior Penetration Tester & Red Teamer",
                "company": "Potomac Cyber Security",
                "location": "Washington, DC",
                "period": "2021 - Present",
                "bullets": [
                    "Executed 30+ comprehensive red team engagements and simulated APT attack vectors against Fortune 500 networks.",
                    "Discovered 4 zero-day vulnerabilities in enterprise web application appliances, coordinating responsible disclosure.",
                    "Assessed cloud infrastructure security posture across AWS and Azure, exploiting complex IAM trust policy misconfigurations."
                ]
            },
            {
                "role": "Security Analyst & Pen Tester",
                "company": "Capitol Defense Labs",
                "location": "Arlington, VA",
                "period": "2017 - 2021",
                "bullets": [
                    "Conducted web application vulnerability assessments using Burp Suite and manual code reviews.",
                    "Wrote automated exploit payloads and post-exploitation reporting scripts in Python."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Computer Security & Forensics",
            "school": "George Mason University",
            "year": "2017"
        },
        "projects": [
            {
                "title": "CloudEscalate: AWS IAM Privilege Escalation Tool",
                "tech": "Python, Boto3, AWS IAM API",
                "desc": "Built an automated penetration testing scanner mapping 25+ distinct paths to administrator privilege escalation in AWS."
            }
        ],
        "certifications": ["Offensive Security Certified Professional (OSCP)", "Offensive Security Certified Expert (OSCE)", "GIAC Cloud Penetration Tester (GCPN)"]
    },
    {
        "filename": "Fiona_Gallagher.pdf",
        "format": "pdf",
        "name": "Fiona Gallagher",
        "title": "Mid-Level UI/UX Frontend Engineer",
        "email": "fiona.gallagher@uicraft.design",
        "phone": "+1 (555) 345-6785",
        "location": "Chicago, IL",
        "linkedin": "linkedin.com/in/fiona-gallagher-frontend",
        "github": "github.com/fgallagher-ui",
        "summary": "Design-centric Frontend Engineer with 3+ years of experience transforming complex UX flows into fluid, accessible web interfaces using React, Vue.js, TypeScript, TailwindCSS, and Next.js. Passionate about micro-interactions, responsive typography, and atomic component systems.",
        "skills": {
            "Frontend Tech": "React, Vue.js, Next.js, TypeScript, JavaScript, TailwindCSS, CSS Modules, Framer Motion",
            "Design Tools": "Figma, Adobe XD, Storybook, Zeplin",
            "Standards": "Web Accessibility (WCAG 2.1 AA), Core Web Vitals, Cross-browser Compatibility",
            "Testing & Build": "Jest, React Testing Library, Vite, npm, Git"
        },
        "experience": [
            {
                "role": "Frontend UI Engineer",
                "company": "WindyCity Digital Agency",
                "location": "Chicago, IL",
                "period": "2023 - Present",
                "bullets": [
                    "Engineered 40+ modular UI components in React and TypeScript documented thoroughly in Storybook.",
                    "Integrated smooth micro-animations and route transitions using Framer Motion, boosting user session time by 22%.",
                    "Audited and remediated accessibility deficiencies across company websites to achieve WCAG 2.1 AA compliance."
                ]
            },
            {
                "role": "Junior Web Designer & Developer",
                "company": "Lakeview Creative",
                "location": "Chicago, IL",
                "period": "2021 - 2023",
                "bullets": [
                    "Built client marketing websites using Vue.js, TailwindCSS, and headless CMS integrations.",
                    "Collaborated closely with branding directors to establish unified typography scales and dark/light theme tokens."
                ]
            }
        ],
        "education": {
            "degree": "B.A. in Web Design & Digital Communications",
            "school": "DePaul University",
            "year": "2021"
        },
        "projects": [
            {
                "title": "MotionKit: Animated Component Library",
                "tech": "React, TypeScript, TailwindCSS, Framer Motion",
                "desc": "Built an open-source animation component library with pre-built accessible modals, carousels, and dropdown menus."
            }
        ],
        "certifications": ["Interaction Design Foundation Certified UX Professional"]
    },
    {
        "filename": "Gregory_House.docx",
        "format": "docx",
        "name": "Gregory House",
        "title": "Senior Healthcare AI & Bioinformatics Data Scientist",
        "email": "gregory.house@biomedai.org",
        "phone": "+1 (555) 456-7896",
        "location": "Princeton, NJ",
        "linkedin": "linkedin.com/in/gregory-house-bioai",
        "github": "github.com/ghouse-bioai",
        "summary": "Senior Computational Biologist and AI Researcher with 8+ years of experience applying deep learning and statistical modeling to genomic sequencing, protein structure prediction, and electronic health record (EHR) analytics. Master of Python, PyTorch, Scikit-learn, Biopython, SQL, and HIPAA-compliant data pipelines.",
        "skills": {
            "AI & Data Science": "PyTorch, TensorFlow, Scikit-learn, Pandas, NumPy, XGBoost, SciPy",
            "Bioinformatics": "Biopython, GATK, Nextflow, AlphaFold, BLAST, SAMtools",
            "Clinical Data": "EHR standards (FHIR, HL7), MIMIC-IV dataset, Survival Analysis, Causal Inference",
            "Cloud & Infra": "AWS (HealthOmics, S3, SageMaker), Docker, Linux, Slurm, Git"
        },
        "experience": [
            {
                "role": "Senior Healthcare AI Scientist",
                "company": "Plainsboro BioTech Labs",
                "location": "Princeton, NJ",
                "period": "2020 - Present",
                "bullets": [
                    "Trained deep graph neural networks in PyTorch for drug-target interaction screening, shortening early discovery cycle by 40%.",
                    "Architected HIPAA-compliant clinical outcome prediction pipelines ingesting 3M+ longitudinal hospital patient records.",
                    "Published 3 peer-reviewed studies in computational biology journals on transformer models in antibody design."
                ]
            },
            {
                "role": "Bioinformatics Scientist",
                "company": "Jersey Genomics Institute",
                "location": "New Brunswick, NJ",
                "period": "2016 - 2020",
                "bullets": [
                    "Constructed scalable Nextflow genomic variant calling pipelines on Slurm HPC clusters.",
                    "Performed differential gene expression analysis and survival curve modeling in Python and R."
                ]
            }
        ],
        "education": {
            "degree": "Ph.D. in Computational Biology & Machine Learning",
            "school": "Princeton University",
            "year": "2016"
        },
        "projects": [
            {
                "title": "BioGraphNN: Molecular Property Predictor",
                "tech": "PyTorch Geometric, RDKit, Python, Docker",
                "desc": "Built an open-source graph neural network predicting small-molecule solubility and metabolic toxicity."
            }
        ],
        "certifications": ["AWS Certified Machine Learning - Specialty", "NIH Certified Clinical Data Research Investigator"]
    },
    {
        "filename": "Harper_Lee.pdf",
        "format": "pdf",
        "name": "Harper Lee",
        "title": "Junior Cloud & Infrastructure Support Engineer",
        "email": "harper.lee@cloudops.io",
        "phone": "+1 (555) 567-8907",
        "location": "Nashville, TN",
        "linkedin": "linkedin.com/in/harper-lee-cloud",
        "github": "github.com/hlee-cloud",
        "summary": "Dedicated Cloud Operations and Support Engineer with 2+ years of experience monitoring infrastructure health, resolving tier-2 cloud incidents, and writing automation scripts. Proficient in Linux, Bash, AWS core services, Docker, Python, and Terraform basics. Passionate about cloud security and DevOps best practices.",
        "skills": {
            "Cloud & Systems": "AWS (EC2, S3, IAM, CloudWatch, Route53), Linux (Ubuntu, CentOS), Docker basic",
            "Scripting & Tools": "Bash, Python, Git, Terraform basic, Jira, Confluence",
            "Networking": "TCP/IP, DNS, VPNs, Subnets, Security Groups, SSH"
        },
        "experience": [
            {
                "role": "Cloud Support Associate",
                "company": "MusicCity Tech Systems",
                "location": "Nashville, TN",
                "period": "2022 - Present",
                "bullets": [
                    "Monitored AWS CloudWatch metrics and alerts, triaging and remediating 40+ operational tickets weekly.",
                    "Automated routine server patching and disk cleanup operations using Bash scripts and AWS Systems Manager.",
                    "Assisted platform team in containerizing internal documentation wikis using Docker."
                ]
            }
        ],
        "education": {
            "degree": "B.S. in Information Systems",
            "school": "Vanderbilt University",
            "year": "2022"
        },
        "projects": [
            {
                "title": "Automated CloudWatch Alarm Deployer",
                "tech": "Python, Boto3, AWS CloudWatch, Terraform",
                "desc": "Built a Python automation script that parses inventory tags and automatically attaches CPU and memory alarms."
            }
        ],
        "certifications": ["AWS Certified Cloud Practitioner", "AWS Certified SysOps Administrator - Associate"]
    },
    {
        "filename": "Ian_Malcolm.docx",
        "format": "docx",
        "name": "Ian Malcolm",
        "title": "Principal AI Safety & Governance Architect",
        "email": "ian.malcolm@aisafety.org",
        "phone": "+1 (555) 678-9018",
        "location": "Cambridge, MA",
        "linkedin": "linkedin.com/in/ian-malcolm-safety",
        "github": "github.com/imalcolm-evals",
        "summary": "Pioneering AI Research Architect with 13+ years of experience leading artificial intelligence alignment, model safety evaluations, red teaming frameworks, and algorithmic governance. Deep technical mastery in Python, PyTorch, RLHF/DPO, mechanistic interpretability, adversarial prompt synthesis, and global AI regulatory standards.",
        "skills": {
            "AI Safety Domains": "Model Alignment, RLHF, DPO, Mechanistic Interpretability, Red Teaming, Jailbreak Mitigation",
            "ML Frameworks": "PyTorch, Transformers, HuggingFace, Ray, Deepspeed, Scikit-learn",
            "Evaluation & Benchmarks": "HELM, MMLU, GSM8K, Custom Safety Evals, Automated LLM-as-a-judge",
            "Policy & Standards": "NIST AI RMF, EU AI Act Compliance, ISO/IEC 42001, AI Ethics Board Leadership"
        },
        "experience": [
            {
                "role": "Principal AI Safety Architect",
                "company": "Veritas Alignment Research",
                "location": "Cambridge, MA",
                "period": "2019 - Present",
                "bullets": [
                    "Direct the safety research group developing automated red-teaming agents that discovered 90+ novel jailbreak prompts in frontier LLMs.",
                    "Formulated reinforcement learning from human feedback (RLHF) and Direct Preference Optimization (DPO) pipelines reducing toxic completions by 98%.",
                    "Advised federal regulatory bodies and corporate boards on compliance with NIST AI Risk Management Framework."
                ]
            },
            {
                "role": "Lead Machine Learning Research Scientist",
                "company": "Boston Intelligence Systems",
                "location": "Boston, MA",
                "period": "2015 - 2019",
                "bullets": [
                    "Conducted fundamental research in deep neural network interpretability and adversarial perturbation defense.",
                    "Published 8 papers at NeurIPS, ICML, and ACL on robust representations and algorithmic fairness."
                ]
            },
            {
                "role": "Senior Software Engineer",
                "company": "New England Tech Labs",
                "location": "Waltham, MA",
                "period": "2011 - 2015",
                "bullets": [
                    "Engineered distributed data processing and statistical analysis engines in Python and C++."
                ]
            }
        ],
        "education": {
            "degree": "Ph.D. in Computer Science & Artificial Intelligence",
            "school": "Massachusetts Institute of Technology (MIT)",
            "year": "2011"
        },
        "projects": [
            {
                "title": "SafetyProbe: Mechanistic Interpretability Suite",
                "tech": "PyTorch, TransformerLens, Python",
                "desc": "Built an open-source toolkit for inspecting internal activation directions and steering residual stream representations."
            }
        ],
        "certifications": ["Fellow of the International Artificial Intelligence Safety Consortium"]
    }
]

def generate_pdf(cand, output_path):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Header
    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(w=0, h=9, text=cand['name'], new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(59, 130, 246)
    pdf.cell(w=0, h=6, text=cand['title'], new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_font('Helvetica', size=9)
    pdf.set_text_color(100, 116, 139)
    contact_str = f"{cand['email']} | {cand['phone']} | {cand['location']} | {cand['linkedin']} | {cand['github']}"
    pdf.multi_cell(w=0, h=4.5, text=contact_str, new_x='LMARGIN', new_y='NEXT')
    
    # Horizontal line
    pdf.set_draw_color(203, 213, 225)
    pdf.set_line_width(0.4)
    pdf.line(pdf.get_x(), pdf.get_y() + 1, 200, pdf.get_y() + 1)
    pdf.ln(3)
    
    # Summary
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(w=0, h=6, text="PROFESSIONAL SUMMARY", new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('Helvetica', size=9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(w=0, h=4.5, text=cand['summary'], new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)
    
    # Skills
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(w=0, h=6, text="TECHNICAL SKILLS", new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('Helvetica', size=9)
    pdf.set_text_color(51, 65, 85)
    for cat, val in cand['skills'].items():
        pdf.multi_cell(w=0, h=4.5, text=f"-  {cat}: {val}", new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)
    
    # Experience
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(w=0, h=6, text="PROFESSIONAL EXPERIENCE", new_x='LMARGIN', new_y='NEXT')
    for exp in cand['experience']:
        pdf.set_font('Helvetica', 'B', 9.5)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(w=120, h=5, text=f"{exp['role']} - {exp['company']}")
        pdf.set_font('Helvetica', 'I', 8.5)
        pdf.set_text_color(100, 116, 139)
        pdf.cell(w=0, h=5, text=f"{exp['period']} | {exp['location']}", new_x='LMARGIN', new_y='NEXT')
        
        pdf.set_font('Helvetica', size=8.5)
        pdf.set_text_color(51, 65, 85)
        for bullet in exp['bullets']:
            pdf.multi_cell(w=0, h=4.2, text=f"-  {bullet}", new_x='LMARGIN', new_y='NEXT')
        pdf.ln(1.5)
    
    # Education
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(w=0, h=6, text="EDUCATION", new_x='LMARGIN', new_y='NEXT')
    edu = cand['education']
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(w=120, h=4.5, text=f"{edu['degree']} - {edu['school']}")
    pdf.set_font('Helvetica', size=8.5)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(w=0, h=4.5, text=f"Graduated {edu['year']}", new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)
    
    # Key Projects
    if 'projects' in cand and cand['projects']:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(24, 43, 73)
        pdf.cell(w=0, h=6, text="KEY PROJECTS", new_x='LMARGIN', new_y='NEXT')
        for prj in cand['projects']:
            pdf.set_font('Helvetica', 'B', 9)
            pdf.set_text_color(30, 41, 59)
            pdf.multi_cell(w=0, h=4.5, text=f"* {prj['title']} [{prj['tech']}]", new_x='LMARGIN', new_y='NEXT')
            pdf.set_font('Helvetica', size=8.5)
            pdf.set_text_color(71, 85, 105)
            pdf.multi_cell(w=0, h=4.2, text=f"   {prj['desc']}", new_x='LMARGIN', new_y='NEXT')
        pdf.ln(2)
        
    # Certifications
    if 'certifications' in cand and cand['certifications']:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(24, 43, 73)
        pdf.cell(w=0, h=6, text="CERTIFICATIONS", new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('Helvetica', size=8.5)
        pdf.set_text_color(71, 85, 105)
        pdf.multi_cell(w=0, h=4.2, text=" | ".join(cand['certifications']), new_x='LMARGIN', new_y='NEXT')
        
    pdf.output(output_path)

def generate_docx(cand, output_path):
    doc = docx.Document()
    
    # Set standard margins (0.75 in)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
    # Header: Name
    title_p = doc.add_paragraph()
    r_name = title_p.add_run(cand['name'])
    r_name.font.name = 'Calibri'
    r_name.font.size = Pt(20)
    r_name.font.bold = True
    r_name.font.color.rgb = RGBColor(24, 43, 73)
    
    # Subtitle
    sub_p = doc.add_paragraph()
    r_title = sub_p.add_run(cand['title'])
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(59, 130, 246)
    
    # Contact
    contact_p = doc.add_paragraph()
    contact_str = f"{cand['email']}  |  {cand['phone']}  |  {cand['location']}  |  {cand['linkedin']}  |  {cand['github']}"
    r_contact = contact_p.add_run(contact_str)
    r_contact.font.name = 'Calibri'
    r_contact.font.size = Pt(9.5)
    r_contact.font.color.rgb = RGBColor(100, 116, 139)
    
    # Section Heading helper
    def add_section_heading(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        r = h.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(24, 43, 73)
        
    # Summary
    add_section_heading("PROFESSIONAL SUMMARY")
    sum_p = doc.add_paragraph()
    sum_p.paragraph_format.space_after = Pt(4)
    r_sum = sum_p.add_run(cand['summary'])
    r_sum.font.name = 'Calibri'
    r_sum.font.size = Pt(10)
    
    # Skills
    add_section_heading("TECHNICAL SKILLS")
    for cat, val in cand['skills'].items():
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(1)
        r_cat = sp.add_run(f"{cat}: ")
        r_cat.font.name = 'Calibri'
        r_cat.font.size = Pt(10)
        r_cat.font.bold = True
        r_val = sp.add_run(val)
        r_val.font.name = 'Calibri'
        r_val.font.size = Pt(10)
        
    # Experience
    add_section_heading("PROFESSIONAL EXPERIENCE")
    for exp in cand['experience']:
        ep = doc.add_paragraph()
        ep.paragraph_format.space_before = Pt(4)
        ep.paragraph_format.space_after = Pt(1)
        
        r_exp_title = ep.add_run(f"{exp['role']} - {exp['company']}")
        r_exp_title.font.name = 'Calibri'
        r_exp_title.font.size = Pt(10.5)
        r_exp_title.font.bold = True
        
        r_exp_sub = ep.add_run(f" ({exp['period']} | {exp['location']})")
        r_exp_sub.font.name = 'Calibri'
        r_exp_sub.font.size = Pt(9.5)
        r_exp_sub.font.italic = True
        r_exp_sub.font.color.rgb = RGBColor(100, 116, 139)
        
        for bullet in exp['bullets']:
            bp = doc.add_paragraph(style='List Bullet')
            bp.paragraph_format.space_before = Pt(0)
            bp.paragraph_format.space_after = Pt(1)
            r_b = bp.add_run(bullet)
            r_b.font.name = 'Calibri'
            r_b.font.size = Pt(9.5)
            
    # Education
    add_section_heading("EDUCATION")
    edu_p = doc.add_paragraph()
    edu_p.paragraph_format.space_before = Pt(2)
    edu_p.paragraph_format.space_after = Pt(2)
    edu = cand['education']
    r_edu = edu_p.add_run(f"{edu['degree']} - {edu['school']} (Graduated {edu['year']})")
    r_edu.font.name = 'Calibri'
    r_edu.font.size = Pt(10)
    
    # Projects
    if 'projects' in cand and cand['projects']:
        add_section_heading("KEY PROJECTS")
        for prj in cand['projects']:
            pp = doc.add_paragraph()
            pp.paragraph_format.space_before = Pt(2)
            pp.paragraph_format.space_after = Pt(1)
            r_pt = pp.add_run(f"{prj['title']} [{prj['tech']}]\n")
            r_pt.font.name = 'Calibri'
            r_pt.font.size = Pt(10)
            r_pt.font.bold = True
            r_pd = pp.add_run(prj['desc'])
            r_pd.font.name = 'Calibri'
            r_pd.font.size = Pt(9.5)
            
    # Certifications
    if 'certifications' in cand and cand['certifications']:
        add_section_heading("CERTIFICATIONS")
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(2)
        cp.paragraph_format.space_after = Pt(2)
        r_cert = cp.add_run(" | ".join(cand['certifications']))
        r_cert.font.name = 'Calibri'
        r_cert.font.size = Pt(9.5)
        
    doc.save(output_path)

def main():
    print(f"Generating {len(CANDIDATES)} resumes in {OUTPUT_DIR}...")
    for idx, cand in enumerate(CANDIDATES, 1):
        target_path = os.path.join(OUTPUT_DIR, cand['filename'])
        if cand['format'] == 'pdf':
            generate_pdf(cand, target_path)
            print(f"[{idx}/35] Created PDF: {cand['filename']}")
        elif cand['format'] == 'docx':
            generate_docx(cand, target_path)
            print(f"[{idx}/35] Created DOCX: {cand['filename']}")
    print("All 35 resumes successfully created!")

if __name__ == "__main__":
    main()
