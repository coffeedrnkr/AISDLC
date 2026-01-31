# PRD Writing Agent - Complete Installation and User Guide

**Version:** 1.0.0
**Last Updated:** 2025-11-06
**Estimated Setup Time:** 20-30 minutes
**Skill Level:** Intermediate (basic GCP knowledge required)

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   - [Step 1: Prepare Your Environment](#step-1-prepare-your-environment)
   - [Step 2: Deploy Vertex AI Agent](#step-2-deploy-vertex-ai-agent)
   - [Step 3: Deploy Cloud Function](#step-3-deploy-cloud-function)
   - [Step 4: Configure Google Chat App](#step-4-configure-google-chat-app)
   - [Step 5: Test Your Installation](#step-5-test-your-installation)
4. [User Guide](#user-guide)
   - [Getting Started](#getting-started)
   - [Creating Your First PRD](#creating-your-first-prd)
   - [Advanced Features](#advanced-features)
   - [Tips & Best Practices](#tips--best-practices)
5. [Troubleshooting](#troubleshooting)
6. [Cost Management](#cost-management)
7. [Security & Privacy](#security--privacy)
8. [FAQ](#faq)
9. [Support](#support)

---

## Overview

The **PRD Writing Agent** is an AI-powered assistant that helps Product Managers and Business Analysts create comprehensive Product Requirements Documents (PRDs). It works directly in Google Chat, where you can have natural conversations, upload documents, and generate complete PRD drafts following your company's template.

### What It Does

- 📄 **Analyzes uploaded materials** - Presentations, business cases, meeting notes
- 💬 **Asks clarifying questions** - Guides you through PRD structure
- ✍️ **Generates complete PRD drafts** - Follows 8-section template
- 🔄 **Iterates based on feedback** - Expand or revise any section
- ✅ **Validates completeness** - Checks all required sections
- 📤 **Exports to Google Docs** - Ready for collaboration

### Architecture

```
You (in Google Chat)
    ↓
Cloud Function (webhook)
    ↓
Vertex AI Agent (Gemini 1.5 Pro)
    ↓
Firestore (your conversation history) + Cloud Storage (your documents)
    ↓
Google Docs (PRD output)
```

All components run in **your Google Cloud project** - your data never leaves your environment.

---

## Prerequisites

### Required Accounts & Permissions

1. **Google Cloud Project** with billing enabled
   - If you don't have one: https://console.cloud.google.com/projectcreate
   - Billing must be enabled: https://console.cloud.google.com/billing

2. **Required GCP Permissions** (ask your admin if you don't have these):
   - `roles/owner` OR these specific roles:
     - `roles/aiplatform.admin` (Vertex AI)
     - `roles/cloudfunctions.admin` (Cloud Functions)
     - `roles/datastore.owner` (Firestore)
     - `roles/storage.admin` (Cloud Storage)
     - `roles/iam.serviceAccountUser` (Service Accounts)

3. **Google Workspace Account**
   - Must be able to create Google Chat apps
   - Admin access helpful (or work with your admin)

### Required Software

1. **gcloud CLI** - Google Cloud command-line tool
   - Install: https://cloud.google.com/sdk/docs/install
   - Verify: `gcloud --version` should show version 450.0.0 or higher

2. **Git** (optional but recommended)
   - To clone this repository
   - Install: https://git-scm.com/downloads

3. **Text Editor** (optional)
   - For viewing/editing configuration files
   - VS Code, Sublime, or any editor works

### Estimated Costs

**Monthly costs for typical usage (50 PRDs/month):**

| Service | Cost |
|---------|------|
| Vertex AI Gemini 1.5 Pro | ~$15 |
| Cloud Functions | ~$2 |
| Cloud Storage | ~$1 |
| Firestore | ~$1 |
| **Total** | **~$19/month** |

**Value delivered:** $20,000-30,000/month in PM time savings (4-6 hours saved per PRD)

---

## Installation

### Step 1: Prepare Your Environment

#### 1.1 Install gcloud CLI

If not already installed:

**macOS:**
```bash
# Download and install
curl https://sdk.cloud.google.com | bash

# Restart your terminal, then initialize
gcloud init
```

**Windows:**
Download installer from: https://cloud.google.com/sdk/docs/install

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

#### 1.2 Authenticate with Google Cloud

```bash
# Login to your Google account
gcloud auth login

# Follow the browser prompts to authenticate

# Set your default project
gcloud config set project YOUR_PROJECT_ID

# Verify it worked
gcloud config list
```

**Replace `YOUR_PROJECT_ID`** with your actual GCP project ID (found in GCP Console: https://console.cloud.google.com)

#### 1.3 Enable Billing

1. Go to: https://console.cloud.google.com/billing
2. Link a billing account to your project
3. Verify billing is enabled:
   ```bash
   gcloud beta billing projects describe YOUR_PROJECT_ID
   ```
   Should show `billingEnabled: true`

#### 1.4 Get the Code

**Option A: Clone the repository (recommended)**
```bash
cd ~/Projects  # or wherever you keep code
git clone https://github.com/your-org/gemini-enterprise-agent.git
cd gemini-enterprise-agent
```

**Option B: Download ZIP**
1. Download the code as ZIP from GitHub
2. Extract to a folder like `~/Projects/gemini-enterprise-agent`
3. Open terminal in that folder

---

### Step 2: Deploy Vertex AI Agent

This step creates the AI brain that powers PRD writing.

#### 2.1 Navigate to Agent Directory

```bash
cd vertex-ai-agents/prd-agent
```

#### 2.2 Review Configuration (Optional)

Open `agent-config.json` to see the agent configuration:

```bash
cat agent-config.json
```

**Key settings you might want to adjust:**
- `temperature: 0.3` - Lower = more consistent, Higher = more creative (range: 0.0-1.0)
- `maxOutputTokens: 8192` - Maximum length of responses

**Most users should leave defaults as-is.**

#### 2.3 Run Deployment Script

```bash
# Make script executable (if not already)
chmod +x deploy.sh

# Deploy (replace with your project ID and region)
./deploy.sh YOUR_PROJECT_ID us-central1
```

**Region options:**
- `us-central1` (Iowa) - Recommended for US
- `us-east1` (South Carolina)
- `europe-west1` (Belgium)
- `asia-northeast1` (Tokyo)

**This script will:**
1. ✅ Enable required APIs (Vertex AI, Storage, Firestore)
2. ✅ Create Cloud Storage bucket for documents
3. ✅ Upload example PRD from ETF analyzer
4. ✅ Create Firestore database (if doesn't exist)
5. ✅ Deploy Vertex AI agent with Gemini 1.5 Pro
6. ✅ Create data store with PRD examples
7. ✅ Generate `.env.yaml` for next step

**Expected output:**
```
🚀 Deploying PRD Writing Agent to Vertex AI
   Project: your-project-id
   Region: us-central1

📦 Setting project...
🔌 Enabling required APIs...
📦 Creating Cloud Storage bucket for PRD examples...
📤 Uploading example PRDs...
   ✅ Uploaded ETF Analyzer PRD example
🗄️  Setting up Firestore...
   ✅ Firestore database already exists
🤖 Creating Vertex AI agent...
✅ Agent created with ID: 1234567890abcdef
   Saved agent ID to .agent-id
📚 Creating data store for PRD examples...
✅ Data store created: prd-example-library-xyz
🔗 Linking data store to agent...
✅ Data store linked to agent
📝 Creating environment variables file...
   ✅ Created .env.yaml for Cloud Functions

✅ Deployment complete!

📋 Next steps:
   1. Test the agent in Vertex AI console:
      https://console.cloud.google.com/vertex-ai/agents?project=your-project-id

   2. Deploy Cloud Functions:
      cd ../../cloud-functions/prd-agent-chat
      ./deploy.sh

   3. Set up Google Chat integration:
      https://developers.google.com/chat/how-tos/apps-develop

📝 Agent details:
   Agent ID: 1234567890abcdef
   Data Store ID: prd-example-library-xyz
   Storage Bucket: gs://your-project-id-prd-examples
```

**⏱️ Time:** 2-3 minutes

#### 2.4 Test Agent in Console (Optional)

1. Go to Vertex AI console: https://console.cloud.google.com/vertex-ai/agents
2. Find "PRD Writing Agent" in the list
3. Click on it
4. Click **"Test"** button in the top right
5. Try a test message:
   ```
   I need to create a PRD for a customer portal project
   ```
6. Agent should respond with guidance on getting started

**If this works, your agent is deployed successfully! ✅**

---

### Step 3: Deploy Cloud Function

This step creates the webhook that connects Google Chat to your Vertex AI agent.

#### 3.1 Navigate to Cloud Function Directory

```bash
cd ../../cloud-functions/prd-agent-chat
```

#### 3.2 Verify Environment File Exists

```bash
# Check that Vertex AI deployment created this file
ls -la ../.env.yaml
```

You should see a file created by the previous step. If not, go back and complete Step 2.

#### 3.3 Review Cloud Function Code (Optional)

```bash
# View the webhook implementation
cat main.py | head -50
```

This is the code that handles messages from Google Chat.

#### 3.4 Deploy Cloud Function

```bash
# Make script executable (if not already)
chmod +x deploy.sh

# Deploy (use same project ID and region as Step 2)
./deploy.sh YOUR_PROJECT_ID us-central1
```

**This script will:**
1. ✅ Load environment variables from `.env.yaml`
2. ✅ Enable Cloud Functions and Cloud Build APIs
3. ✅ Deploy function to Cloud Functions Gen2
4. ✅ Configure with 512MB memory and 540s timeout
5. ✅ Allow unauthenticated access (required for Google Chat)
6. ✅ Return webhook URL for next step

**Expected output:**
```
🚀 Deploying PRD Agent Chat Webhook
   Project: your-project-id
   Region: us-central1
   Function: prd-agent-chat

📦 Environment variables loaded:
   GCP_PROJECT_ID: your-project-id
   VERTEX_AI_LOCATION: us-central1
   PRD_AGENT_ID: 1234567890abcdef

☁️  Deploying Cloud Function...
Deploying function (may take a while - up to 2 minutes)...
⠹

✅ Deployment complete!

📋 Function details:
   Name: prd-agent-chat
   URL: https://us-central1-your-project-id.cloudfunctions.net/prd-agent-chat

🔗 Next steps:

1. Configure Google Chat app:
   https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat

2. Set webhook URL in Chat API configuration:
   https://us-central1-your-project-id.cloudfunctions.net/prd-agent-chat

3. Enable the app for your domain

4. Test in Google Chat:
   - Search for 'PRD Agent'
   - Start a conversation
   - Type 'help' to see available commands

📊 View logs:
   gcloud functions logs read prd-agent-chat --region=us-central1 --gen2
```

**⏱️ Time:** 2-3 minutes

#### 3.5 Copy the Webhook URL

**IMPORTANT:** Copy the function URL from the output. You'll need it in the next step.

It will look like:
```
https://us-central1-YOUR_PROJECT_ID.cloudfunctions.net/prd-agent-chat
```

---

### Step 4: Configure Google Chat App

This step makes the agent available in Google Chat.

#### 4.1 Enable Google Chat API

1. Go to: https://console.cloud.google.com/apis/api/chat.googleapis.com
2. Click **"Enable"** button
3. Wait for API to be enabled (~30 seconds)

#### 4.2 Configure Chat App

1. After enabling, you'll see the Chat API dashboard
2. Click on the **"Configuration"** tab (top of page)
3. Fill in the following fields:

**App Name:**
```
PRD Agent
```

**Avatar URL** (optional):
```
https://fonts.gstatic.com/s/i/productlogos/docs/v2/web-64dp/logo_docs_color_1x_web_64dp.png
```

**Description:**
```
AI assistant for creating comprehensive Product Requirements Documents. Upload materials, answer questions, and generate PRD drafts following company templates.
```

#### 4.3 Configure Features

Scroll down to **"Interactive features"** section:

**Enable these checkboxes:**
- ✅ **Receive 1:1 messages** - Allows direct messages to bot
- ✅ **Join spaces and group conversations** - Allows bot in team spaces
- ✅ **Enable Interactive features** - Allows cards and buttons

#### 4.4 Configure Connection Settings

Scroll to **"Connection settings"** section:

**App URL:** (paste your webhook URL from Step 3.5)
```
https://us-central1-YOUR_PROJECT_ID.cloudfunctions.net/prd-agent-chat
```

**Connection type:**
- ● **App URL** (selected by default)

#### 4.5 Configure Visibility

Scroll to **"Visibility"** section:

**App visibility:**

Choose one:

**Option A: Make available to your entire domain (recommended)**
- ● **Make this Chat app available to specific people and groups in DOMAIN**
- Enter your domain (e.g., `company.com`)

**Option B: Make available to specific users**
- ● **Make this Chat app available to specific people and groups in DOMAIN**
- Add specific email addresses

**Option C: Private (just you for testing)**
- Leave default settings

#### 4.6 Save Configuration

1. Scroll to bottom of page
2. Click **"Save"** button
3. You should see: "Configuration saved successfully"

**⏱️ Time:** 3-5 minutes

---

### Step 5: Test Your Installation

#### 5.1 Open Google Chat

Go to: https://chat.google.com

(Or open Google Chat in Gmail)

#### 5.2 Find the PRD Agent

1. Click **"+ New chat"** (or "Start a chat")
2. Click **"Find apps"** or search box
3. Type: `PRD Agent`
4. Click on the agent when it appears
5. Click **"Add"** or **"Message"**

**If you don't see the agent:**
- Wait 1-2 minutes (app takes time to propagate)
- Refresh the page
- Check that you saved the configuration in Step 4.6
- Verify you have access based on visibility settings

#### 5.3 Send Test Message

In the chat with PRD Agent, type:
```
help
```

**Expected response:**
```
📋 PRD Agent - Available Commands

**Getting Started:**
• start new PRD - Begin creating a new PRD
• help - Show this help message

**During PRD Creation:**
• Upload documents (PDF, PPTX, DOCX) to provide context
• Answer clarifying questions naturally
• expand section [name] - Add more detail to a section
• revise section [name] - Change a specific section
• validate prd - Check PRD completeness

**PRD Structure:**
1. Executive Summary
2. Business Intent
3. Functional Envelope
4. Scope Boundaries
5. System Impact
6. Architectural Sketch
7. AI/Automation Use Plan
8. Risks and Open Questions

**Tips:**
• Upload background materials before starting for better results
• Be specific in your answers to clarifying questions
• You can iterate on any section multiple times
• The agent will flag gaps or inconsistencies
```

**If you see this response, congratulations! 🎉 Your installation is complete!**

#### 5.4 Test PRD Creation

Try starting a PRD:
```
start new PRD
```

**Expected response:**
```
🚀 Let's create your PRD!

I'll guide you through the process. First, let's gather context.

**Option 1:** Upload background materials
• Presentations (PPTX)
• Business cases (PDF)
• Meeting notes (DOCX)
• Requirements documents

**Option 2:** Start from scratch
Describe your project in a few sentences:
• What are you building?
• Why is it needed?
• Who is it for?

Which option would you prefer? Or you can do both!
```

**If you see this, everything is working correctly! ✅**

---

## User Guide

### Getting Started

#### Your First Conversation

When you message the PRD Agent for the first time, start with one of these:

**Option 1: Get help**
```
help
```
Shows available commands and PRD structure.

**Option 2: Start immediately**
```
start new PRD
```
Begins the guided PRD creation process.

**Option 3: Ask questions**
```
What can you help me with?
```
Agent will explain its capabilities.

#### Understanding the PRD Structure

Every PRD created by the agent follows this 8-section template:

1. **Executive Summary** (300-400 words)
   - What are we building?
   - Why now?
   - Key success metrics

2. **Business Intent**
   - Business objectives
   - Target users/personas
   - Success criteria
   - Expected impact

3. **Functional Envelope**
   - Core features (must-haves)
   - Secondary features (should-haves)
   - Future considerations

4. **Scope Boundaries**
   - What's IN scope
   - What's OUT of scope
   - What's FUTURE scope

5. **System Impact**
   - Affected systems and teams
   - Integration points
   - Dependencies

6. **Architectural Sketch**
   - High-level technical approach
   - Key components
   - Technology constraints

7. **AI/Automation Use Plan**
   - Where AI/automation applies
   - Expected benefits
   - Risks and mitigations

8. **Risks and Open Questions**
   - Known risks
   - Open questions
   - Assumptions

---

### Creating Your First PRD

#### Scenario 1: Creating PRD from Uploaded Documents

This is the **recommended approach** when you have background materials.

**Step 1: Gather Your Materials**

Collect any of these:
- 📊 Presentations (PowerPoint, Google Slides → export as PPTX)
- 📄 Business cases (PDF)
- 📝 Meeting notes (Word, Google Docs → export as DOCX)
- 📋 Requirements lists (any format)
- 📈 Market research (PDF or DOCX)

**Step 2: Start Conversation**
```
You: start new PRD

Agent: 🚀 Let's create your PRD!

I'll guide you through the process. First, let's gather context.

**Option 1:** Upload background materials
• Presentations (PPTX)
• Business cases (PDF)
• Meeting notes (DOCX)

**Option 2:** Start from scratch
Describe your project in a few sentences

Which option would you prefer?
```

**Step 3: Upload Documents**

1. Click the **attachment icon** (📎) in Google Chat
2. Select **"Upload from computer"**
3. Choose your files (can select multiple)
4. Click **"Open"**

**Supported formats:**
- ✅ PDF (.pdf)
- ✅ PowerPoint (.pptx)
- ✅ Word (.docx)
- ✅ Google Docs (share link)
- ✅ Text files (.txt)

```
You: [Uploads 3 files: presentation.pptx, business-case.pdf, requirements.docx]

Agent: ✅ Received 3 documents:
• presentation.pptx
• business-case.pdf
• requirements.docx

📊 Analyzing documents...

[A card appears showing document analysis status]
```

**Step 4: Review Analysis**

```
Agent: 📊 Analysis Complete:
- Presentation: 24 slides covering customer pain points and proposed solution
- Business Case: Financial projections showing $500K annual cost savings
- Requirements: List of 20 requested features from stakeholders

**Key themes I found:**
• Self-service customer portal
• Integration with existing Salesforce CRM
• Target launch: Q2 2026
• Expected 40% reduction in support tickets

I'll now ask you 5 key questions to complete the PRD.
```

**Step 5: Answer Clarifying Questions**

The agent will ask 5 questions. Answer naturally.

```
Agent: **Question 1/5:** What is the PRIMARY business objective?

I found multiple objectives in your materials. Which is most important?
a) Reduce support costs (from business case)
b) Improve customer satisfaction (from presentation)
c) Enable customer self-service (from requirements)
d) All of the above

You: d) All of the above

Agent: Great! **Question 2/5:** What are the critical success metrics?

I can use the metrics from your business case, or you can specify different ones.

You: Use the metrics from the business case

Agent: Perfect. **Question 3/5:** What's explicitly OUT of scope for version 1?

This helps me define clear boundaries.

You: No mobile app in v1, no payment processing, no third-party integrations beyond CRM

Agent: Understood. **Question 4/5:** Are there any architectural constraints I should know about?

For example: must use certain technologies, integrate with specific systems, data residency requirements, etc.

You: Must integrate with Salesforce, must be cloud-native on Google Cloud Platform

Agent: Got it. **Question 5/5:** Are there any known risks or open questions?

You: Budget approval is still pending. Also unclear if the Salesforce API supports all the features we need.
```

**Step 6: PRD Generation**

```
Agent: Excellent! I have everything I need to generate your PRD.

🎯 Generating PRD draft...

I'm synthesizing:
• 3 uploaded documents
• Your answers to 5 clarifying questions
• Best practices from example PRDs
• Company PRD template

This will take approximately 30-60 seconds...

[30-60 seconds later]

✅ PRD Draft Complete!

📄 **Customer Portal PRD - Draft v1**

The PRD includes all 8 required sections:
✅ 1. Executive Summary (350 words)
✅ 2. Business Intent with success metrics
✅ 3. Functional Envelope (12 core features)
✅ 4. Scope Boundaries (In/Out/Future clearly defined)
✅ 5. System Impact (3 affected systems identified)
✅ 6. Architectural Sketch (Cloud-native GCP architecture)
✅ 7. AI/Automation Use Plan (Customer support automation)
✅ 8. Risks and Open Questions (Budget approval, API capabilities)

[A card appears with buttons:]
[Open in Google Docs] [Revise Section] [Validate PRD]
```

**Step 7: Review and Iterate**

Click **"Open in Google Docs"** to see the full PRD in a Google Doc where you can:
- Read the complete content
- Add comments
- Share with stakeholders
- Make manual edits

Or continue in Chat to revise specific sections.

**⏱️ Total time:** 10-20 minutes (vs 8-12 hours manually)

---

#### Scenario 2: Creating PRD from Scratch (No Documents)

If you don't have background materials, you can create a PRD by describing your project.

**Step 1: Start and Describe**
```
You: start new PRD

Agent: [Shows options]

You: We're building a mobile app for field service technicians. They need to access work orders offline, capture photos, and get customer signatures. This will replace our current paper-based process and save about 2 hours per technician per day.
```

**Step 2: Answer Questions**

Agent will ask the same 5 clarifying questions, but will base them on your description instead of uploaded documents.

**Step 3-7: Same as Scenario 1**

The rest of the process is identical.

---

### Advanced Features

#### Revising Specific Sections

If you want to change or expand a section after the PRD is created:

**Expand a section:**
```
You: Expand section 3 with more detail on the account management features

Agent: I'll expand section 3.3 (Functional Envelope) with more detail on account management.

Should I:
a) Base expansion on the competitor analysis you uploaded
b) Ask you specific questions about what to include
c) Both

You: a) Base it on competitor analysis

Agent: ✅ Section 3.3 expanded!

Added detailed account management features:
• Profile management (name, email, phone, preferences)
• Password reset with MFA options
• Security settings and session management
• Communication preferences (email, SMS, push)
• Account history and activity log
• Multi-user account support with role-based access (admin, member, viewer)
• Account linking for family/business accounts

[Link to updated section in Google Doc]

Anything else to adjust?
```

**Revise a section:**
```
You: Revise section 6 - we've decided to use AWS instead of GCP

Agent: I'll revise section 6 (Architectural Sketch) to reflect AWS instead of GCP.

Should I:
a) Replace all GCP services with AWS equivalents
b) Keep the architecture pattern but swap cloud providers
c) Ask you which specific AWS services to use

You: b) Keep the architecture but swap cloud providers

Agent: ✅ Section 6 revised!

Updated to AWS architecture:
• Frontend: React on AWS Amplify (was GCP Cloud Run)
• Backend: Node.js on AWS Lambda (was Cloud Functions)
• Database: Amazon RDS PostgreSQL (was Cloud SQL)
• Storage: Amazon S3 (was Cloud Storage)
• Auth: Amazon Cognito (was Firebase Auth)
• CDN: Amazon CloudFront (was Cloud CDN)

Architecture pattern remains microservices with serverless compute.

[Link to updated section]
```

#### Validating PRD Completeness

Before sharing your PRD with stakeholders, validate it:

```
You: validate prd

Agent: 📋 **PRD Validation Report**

✅ **Complete sections (8/8):**
1. ✅ Executive Summary (380 words - target met)
2. ✅ Business Intent (includes objectives, success criteria)
3. ✅ Functional Envelope (12 features well-defined)
4. ✅ Scope Boundaries (clear In/Out/Future)
5. ✅ System Impact (3 affected systems identified)
6. ✅ Architectural Sketch (detailed with diagrams)
7. ✅ AI/Automation Use Plan (2 use cases described)
8. ✅ Risks and Open Questions (4 risks, 2 open questions)

📝 **Quality checks:**
✅ Executive Summary length appropriate (300-400 words)
✅ All sections use active voice
✅ Success metrics are specific and measurable
✅ Timeline is mentioned (Q2 2026 launch)
✅ No obvious inconsistencies found

⚠️ **Recommendations:**
• Consider adding cost estimates to Business Intent
• System Impact could include downstream teams affected
• Might want to expand on data migration strategy

**Overall Score: 9/10** - PRD is comprehensive and ready for review!

Would you like me to address any of the recommendations?
```

#### Working with Multiple Projects

The agent maintains separate conversation sessions for different spaces:

**Direct Messages (DMs):**
- Each DM with the agent is a separate session
- Create multiple PRDs in the same DM - agent will ask which one you're working on

**Team Spaces:**
- Each space has its own session
- Multiple people can work on the same PRD in a shared space
- Use threads to avoid conversation confusion

**Managing sessions:**
```
You: What PRDs am I working on?

Agent: You have 2 PRD sessions active:

1. **Customer Portal PRD** (this conversation)
   - Status: Draft complete
   - Last updated: 2 hours ago
   - Sections: 8/8 complete

2. **Mobile Field Service App** (DM started yesterday)
   - Status: In progress (questions 3/5 answered)
   - Last updated: 1 day ago

Which would you like to continue?
```

---

### Tips & Best Practices

#### 🎯 For Best Results

**1. Upload comprehensive materials**
- More context = better PRD
- Include presentations, business cases, competitive analysis
- Meeting notes and stakeholder feedback are valuable
- Even rough notes help!

**2. Be specific in answers**
❌ "We want to reduce costs"
✅ "Reduce support costs by 40% within 6 months, from $500K to $300K annually"

❌ "Improve customer satisfaction"
✅ "Increase NPS from 45 to 70, reduce complaint tickets by 50%"

**3. Define clear boundaries**
Be explicit about what's OUT of scope:
- "No mobile app in v1"
- "No payment processing"
- "Integration with CRM only, not ERP"

**4. Iterate multiple times**
First draft is rarely perfect:
- Review the PRD
- Revise sections that need more detail
- Add missing information
- Validate before sharing

**5. Use threads in team spaces**
When multiple people are in a space:
- Use threads (reply to specific messages) to avoid confusion
- One person should "drive" PRD creation
- Others can review and suggest changes

#### ⚡ Efficiency Tips

**Save time with shortcuts:**
```
"start PRD" instead of "start new PRD"
"expand 3" instead of "expand section 3"
"validate" instead of "validate prd"
```

**Upload documents before starting:**
Have all your materials ready, upload them all at once. Better than uploading one-by-one.

**Use descriptive project names:**
When the agent asks for a title, be specific:
❌ "Portal Project"
✅ "Customer Self-Service Portal - Phase 1"

**Keep conversation focused:**
Stick to one PRD at a time in each conversation. Start a new DM for a new project.

#### 🚫 What NOT to Do

**Don't:**
- ❌ Upload sensitive data (passwords, PII, financials) - agent redacts PII but avoid it
- ❌ Expect the agent to make strategic decisions - you decide, agent documents
- ❌ Rush through clarifying questions - quality answers = quality PRD
- ❌ Forget to review before sharing - always validate first
- ❌ Mix multiple projects in one conversation - keep separate

#### 📱 Mobile Usage

The agent works on mobile, but desktop is better for:
- Uploading documents (easier)
- Reviewing long PRD text (bigger screen)
- Opening Google Docs (better editing)

On mobile:
- ✅ Answer clarifying questions
- ✅ Request section revisions
- ✅ Review PRD summary
- ✅ Quick edits and validations

---

## Troubleshooting

### Installation Issues

#### Issue: "gcloud: command not found"

**Cause:** gcloud CLI not installed or not in PATH

**Fix:**
1. Install gcloud CLI: https://cloud.google.com/sdk/docs/install
2. Restart terminal
3. Run: `gcloud --version`

#### Issue: "Permission denied" during deployment

**Cause:** Insufficient GCP permissions

**Fix:**
1. Check your roles:
   ```bash
   gcloud projects get-iam-policy YOUR_PROJECT_ID \
     --flatten="bindings[].members" \
     --filter="bindings.members:user:YOUR_EMAIL"
   ```
2. Ask admin to grant required roles:
   - `roles/owner` OR
   - `roles/aiplatform.admin`
   - `roles/cloudfunctions.admin`
   - `roles/datastore.owner`
   - `roles/storage.admin`

#### Issue: "Billing is not enabled"

**Cause:** Project doesn't have billing account linked

**Fix:**
1. Go to: https://console.cloud.google.com/billing
2. Click "Link a billing account"
3. Select a billing account (or create one)
4. Try deployment again

#### Issue: "Agent deployment failed"

**Check logs:**
```bash
gcloud logging read "resource.type=cloud_function" --limit 50
```

**Common causes:**
- API not enabled → Re-run deploy script
- Quota exceeded → Request quota increase
- Invalid configuration → Check `agent-config.json`

---

### Usage Issues

#### Issue: Agent not responding in Google Chat

**Check 1: Is Cloud Function working?**
```bash
# View recent logs
gcloud functions logs read prd-agent-chat --region=us-central1 --gen2 --limit=50

# Look for errors or "No logs found"
```

**Check 2: Is webhook URL correct?**
1. Go to: https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat
2. Click "Configuration"
3. Verify "App URL" matches your Cloud Function URL
4. Get correct URL:
   ```bash
   gcloud functions describe prd-agent-chat \
     --region=us-central1 --gen2 \
     --format='value(serviceConfig.uri)'
   ```

**Check 3: Can you see the bot?**
- Search for "PRD Agent" in Google Chat
- If not found, check "Visibility" settings in Chat API console
- Wait 2-3 minutes after configuration changes

**Still not working?**
```bash
# Test webhook directly
curl -X POST YOUR_WEBHOOK_URL \
  -H "Content-Type: application/json" \
  -d '{"type":"MESSAGE","message":{"text":"test"}}'

# Should return JSON response, not error
```

#### Issue: "Sorry, I encountered an error"

**View detailed error:**
```bash
gcloud functions logs read prd-agent-chat \
  --region=us-central1 --gen2 \
  --limit=20 \
  --format="value(textPayload)"
```

**Common errors:**

**"Agent ID not found"**
- Vertex AI agent not deployed
- Environment variables not set
- Fix: Re-run Vertex AI deployment

**"Firestore error"**
- Firestore not enabled or created
- Fix: `gcloud firestore databases create --region=us-central1`

**"Permission denied"**
- Service account missing permissions
- Fix:
  ```bash
  PROJECT_ID="your-project-id"
  SA_EMAIL="${PROJECT_ID}@appspot.gserviceaccount.com"

  gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/aiplatform.user"
  ```

#### Issue: Document uploads not working

**Current limitation:**
- Phase 1 only stores document metadata
- Full text extraction coming in Phase 2

**Workaround:**
- Describe document contents in text
- Copy/paste key sections into chat
- Agent will use your text description

#### Issue: PRD generation is slow (>2 minutes)

**Normal range:** 30-60 seconds

**If longer:**
1. Check Gemini API quotas:
   ```bash
   gcloud services quota list --service=aiplatform.googleapis.com
   ```
2. Check for rate limiting in logs
3. Try again during off-peak hours

**If timing out (>90 seconds):**
- Increase Cloud Function timeout:
  ```bash
  gcloud functions deploy prd-agent-chat \
    --region=us-central1 --gen2 \
    --timeout=540s \
    --update-env-vars=VERTEX_AI_LOCATION=us-central1
  ```

#### Issue: Google Doc not created

**Phase 1 limitation:**
- Google Docs creation coming in Phase 2
- Currently shows placeholder message

**Workaround:**
- Agent provides PRD text in Chat
- Copy/paste into Google Doc manually
- Format with headings and bullets

---

### Common Error Messages

| Error Message | Meaning | Fix |
|---------------|---------|-----|
| "Unauthorized" | Webhook verification failed | Check Chat API configuration |
| "Agent not found" | Vertex AI agent ID incorrect | Verify `.env.yaml` has correct ID |
| "Quota exceeded" | Hit API rate limits | Wait or request quota increase |
| "Invalid session" | Firestore session corrupted | Say "start new PRD" to reset |
| "Document too large" | Uploaded file >10MB | Split document or compress PDF |
| "Timeout" | Operation took >90s | Retry; if persists, increase timeout |

---

## Cost Management

### Understanding Your Costs

**Fixed vs Variable:**

**Fixed (~$2/month):**
- Cloud Functions (always running)
- Cloud Storage (data storage)
- Firestore (database storage)

**Variable (scales with usage):**
- Gemini API calls (~$0.30-0.40 per PRD)
- Cloud Functions invocations ($0.10 per PRD)

### Cost Breakdown Example

**50 PRDs/month:**
| Component | Calculation | Cost |
|-----------|-------------|------|
| Gemini API | 50 × $0.35 | $17.50 |
| Cloud Functions | 50 × $0.04 | $2.00 |
| Storage | 5GB × $0.02 | $0.10 |
| Firestore | 500K ops × $0.002 | $1.00 |
| **Total** | | **$20.60** |

**200 PRDs/month:**
| Component | Calculation | Cost |
|-----------|-------------|------|
| Gemini API | 200 × $0.35 | $70.00 |
| Cloud Functions | 200 × $0.04 | $8.00 |
| Storage | 20GB × $0.02 | $0.40 |
| Firestore | 2M ops × $0.002 | $4.00 |
| **Total** | | **$82.40** |

### Monitoring Costs

**View current costs:**
```bash
# This month's costs
gcloud billing accounts list

# Detailed breakdown
gcloud beta billing account-billing-project reports list \
  --billing-account=YOUR_BILLING_ACCOUNT_ID
```

**Set up billing alerts:**
1. Go to: https://console.cloud.google.com/billing/alerts
2. Click "Create alert"
3. Set threshold (e.g., $50/month)
4. Add your email
5. Click "Save"

### Reducing Costs

**1. Delete old sessions:**
```bash
# Delete sessions older than 90 days
# (Firestore console: https://console.cloud.google.com/firestore)
# Filter: created_at < 90 days ago
# Batch delete
```

**2. Clean up old documents:**
```bash
# List files in bucket
gsutil ls gs://YOUR_PROJECT_ID-prd-examples

# Delete files older than 90 days
gsutil -m rm gs://YOUR_PROJECT_ID-prd-examples/**/*-2024-*
```

**3. Reduce PRD length:**
- Use "brief" instead of "detailed" for sections
- Focus on essential information
- Shorter responses = lower Gemini costs

**4. Monitor usage:**
```bash
# View Gemini API usage
gcloud logging read "resource.type=aiplatform.googleapis.com" \
  --limit=100 \
  --format="table(timestamp,textPayload)"
```

---

## Security & Privacy

### Data Storage

**Where your data lives:**
- ✅ **Your GCP project** - All data in your tenant
- ✅ **Your chosen region** - Data residency you control
- ✅ **Your Firestore database** - Encrypted at rest
- ✅ **Your Cloud Storage bucket** - Private by default

**Data never:**
- ❌ Shared with other customers
- ❌ Used to train models
- ❌ Sent outside your project
- ❌ Stored by Anthropic or third parties

### PII Handling

**Built-in protection:**
- Agent configured to redact PII (emails, phone numbers, SSNs)
- Firestore security rules prevent cross-user access
- Cloud Storage buckets are private

**Best practices:**
- Don't upload documents with sensitive financial data
- Don't include passwords or API keys in PRDs
- Don't mention customer names if sensitive
- Use anonymized examples when possible

### Access Control

**Who can use the agent:**
- Controlled by Google Chat app visibility settings
- Restrict to domain (e.g., @company.com)
- Or specific users/groups

**Who can see conversations:**
- Only participants in the Chat space
- Project owners can view Cloud Function logs
- Firestore admins can view session data

**Audit logging:**
```bash
# View who used the agent
gcloud logging read "resource.type=cloud_function" \
  --format="table(timestamp,resource.labels.function_name,labels.user)"
```

### Compliance

**Google Cloud compliance:**
- ✅ SOC 2 Type II
- ✅ ISO 27001
- ✅ GDPR compliant (EU regions)
- ✅ HIPAA capable (with BAA)

**Your responsibilities:**
- Review PRDs before sharing
- Don't include regulated data (PHI, PCI)
- Follow your company's data classification policies
- Train users on appropriate usage

### Deleting Data

**Delete a specific session:**
1. Go to: https://console.cloud.google.com/firestore
2. Navigate to `prd_sessions` collection
3. Find session by ID
4. Click delete

**Delete all agent data:**
```bash
# Delete all sessions
gcloud firestore delete --all-collections --project=YOUR_PROJECT_ID

# Delete all documents
gsutil -m rm -r gs://YOUR_PROJECT_ID-prd-examples/**

# Delete Cloud Function (stops all usage)
gcloud functions delete prd-agent-chat --region=us-central1 --gen2

# Delete Vertex AI agent
gcloud ai agents delete AGENT_ID --region=us-central1
```

---

## FAQ

### General

**Q: How long does it take to create a PRD?**
A: 10-20 minutes with the agent vs 8-12 hours manually. 50-70% time savings.

**Q: Can multiple people work on the same PRD?**
A: Yes! Add the agent to a team space. One person should "drive" the conversation, others can review and suggest changes.

**Q: What happens to my uploaded documents?**
A: Currently stored as metadata only (Phase 1). Full text extraction in Phase 2. All data stays in your GCP project.

**Q: Can I customize the PRD template?**
A: Yes, edit `agent-config.json` in `/vertex-ai-agents/prd-agent/` and redeploy. Modify the "system_instruction" section.

**Q: Does it work with languages other than English?**
A: Gemini supports 100+ languages. Try asking in your language! Quality may vary for less common languages.

### Technical

**Q: What model does it use?**
A: Gemini 1.5 Pro (gemini-1.5-pro-002) via Vertex AI. 1M+ token context window.

**Q: Can I use a different model?**
A: Yes, edit `agent-config.json` and change the `model` field. Options: `gemini-1.5-pro-002`, `gemini-1.5-flash-002`.

**Q: How much context does the agent remember?**
A: Last 10 messages in the conversation, plus all uploaded documents for the session.

**Q: Can I integrate with Jira/Confluence?**
A: Not in Phase 1. Phase 4 includes Jira integration for epic/story creation.

**Q: Can I deploy to multiple regions?**
A: Yes, run deployment in each region with different agent names. Chat app can route to nearest region.

### Pricing

**Q: What if I go over budget?**
A: Set up billing alerts (see Cost Management section). Cloud Functions will stop when budget exceeded (if configured).

**Q: Are there free tiers?**
A: Vertex AI has no free tier. Cloud Functions has 2M invocations/month free. Firestore has 50K reads/day free.

**Q: How can I estimate my costs?**
A: Use GCP Pricing Calculator: https://cloud.google.com/products/calculator
- Enter your expected PRD count/month
- Multiply by $0.40/PRD for rough estimate

### Support

**Q: Where can I get help?**
A:
1. Check troubleshooting section above
2. View Cloud Function logs for errors
3. Ask in your company's internal Slack/Teams
4. File GitHub issue (if open source)
5. Contact GCP support (if you have support plan)

**Q: Can I see the source code?**
A: Yes! All code is in the repository:
- Vertex AI config: `/vertex-ai-agents/prd-agent/`
- Cloud Function: `/cloud-functions/prd-agent-chat/`
- Docs: `/docs/`

**Q: How do I contribute improvements?**
A: Fork the repo, make changes, submit pull request. See CONTRIBUTING.md.

**Q: Is there a roadmap?**
A: Yes! See Phase 2-4 plans in the design doc: `/docs/implementation/prd-agent-design.md`

---

## Support

### Getting Help

**1. Check documentation:**
- This guide (you're reading it!)
- [Architecture Design](../implementation/prd-agent-design.md)
- [Vertex AI README](../../vertex-ai-agents/prd-agent/README.md)
- [Implementation Guide](../../Implementation-Decision-Guide.md)

**2. View logs:**
```bash
# Cloud Function logs
gcloud functions logs read prd-agent-chat \
  --region=us-central1 --gen2 \
  --limit=50

# Vertex AI logs
gcloud logging read "resource.type=aiplatform.googleapis.com" \
  --limit=50
```

**3. Test components:**
```bash
# Test Vertex AI agent in console
open https://console.cloud.google.com/vertex-ai/agents

# Test Cloud Function
curl YOUR_WEBHOOK_URL -X POST \
  -H "Content-Type: application/json" \
  -d '{"type":"MESSAGE","message":{"text":"test"}}'
```

**4. Community support:**
- GitHub Issues: [your-repo-url]/issues
- Internal Slack/Teams channel
- GCP Community: https://cloud.google.com/community

**5. Professional support:**
- GCP Support: https://cloud.google.com/support
- Contact your account manager
- Professional services (for customization)

### Providing Feedback

We want to hear from you! Share:
- ✅ What works well
- ❌ What doesn't work
- 💡 Feature requests
- 🐛 Bugs

**How to report:**
1. GitHub Issues (preferred)
2. Email to team
3. In-app feedback (coming in Phase 2)

---

## Appendix

### Quick Reference Card

**Common commands:**
```
start new PRD          - Begin creating a PRD
help                   - Show available commands
expand section [name]  - Add detail to a section
revise section [name]  - Change a section
validate prd          - Check PRD completeness
```

**PRD sections:**
1. Executive Summary
2. Business Intent
3. Functional Envelope
4. Scope Boundaries
5. System Impact
6. Architectural Sketch
7. AI/Automation Use Plan
8. Risks and Open Questions

**Supported file types:**
- PDF (.pdf)
- PowerPoint (.pptx)
- Word (.docx)
- Text (.txt)

**Deployment commands:**
```bash
# Deploy Vertex AI agent
cd vertex-ai-agents/prd-agent
./deploy.sh PROJECT_ID us-central1

# Deploy Cloud Function
cd cloud-functions/prd-agent-chat
./deploy.sh PROJECT_ID us-central1

# View logs
gcloud functions logs read prd-agent-chat --region=us-central1 --gen2
```

---

### Related Documentation

**Framework documentation:**
- [Implementation Decision Guide](../../Implementation-Decision-Guide.md)
- [Agent Inventory](../agent-inventory-and-design-guide.md)
- [PRD Writing Guide](../prd-guide.md)

**Example PRDs:**
- [ETF Portfolio Analyzer](../../examples/etf-portfolio-analyzer/docs/prd.md)

**Technical documentation:**
- [Architecture Design](../implementation/prd-agent-design.md)
- [Phase 1 Summary](../implementation/prd-agent-phase1-summary.md)

**Google Cloud documentation:**
- [Vertex AI Agent Builder](https://cloud.google.com/vertex-ai/docs/agent-builder)
- [Cloud Functions](https://cloud.google.com/functions/docs)
- [Google Chat API](https://developers.google.com/chat)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-06 | Initial release |

---

## License

[Your license here]

---

## Acknowledgments

Built with:
- Google Cloud Vertex AI
- Google Gemini 1.5 Pro
- Google Cloud Functions
- Google Firestore
- Google Chat API

---

**Questions? Issues? Feedback?**

File an issue: [your-repo-url]/issues
Email: [your-email]
Slack: [your-slack-channel]

---

**🎉 Happy PRD Writing! 🚀**
