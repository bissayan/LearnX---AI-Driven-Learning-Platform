# SE Project Directory Structure

## Project Overview
A full-stack educational platform using Vue.js (frontend) and Flask (backend), integrating an AI chatbot TutorX which ensures that every student has access to a personalized tutor, available 24/7, improving doubt resolution, engagement, and learning outcomes.

TutorX is an AI Chatbot integrated in a retrieval-augmented generation (RAG) pipeline using Sentence Transformers to convert lecture materials into vector embeddings stored as Knowledge Base in Vector Database LanceDB. Based on query intent, the system autonomously chooses between retrieving from LanceDB via semantic search or searching the web via DuckDuckGo; Has session memory for upto 25 conversations, and context-aware response generation via OpenRouter API (Google Gemini-2.5-Pro).

The platform handles real-time student features including AI-assisted course content, feedback, coding submissions, instructor content creation, and admin management. Used PyTest for unit testing APIs, and GitHub with CI/CD for version control.  Deadline reminders using SMTP via redis and celery workers.

Tech Stack: Flask, SQLite, jwt, Vue.js (CDN),  LanceDB, Sentence Transformers, phi library, OpenRouter API, Gemini-2.5-Pro, , GitHub (CI/CD), Postman, Celery, Redis, PyTest, JIRA.

Demo Project Working Video Link: https://drive.google.com/drive/folders/1qmfaodj9NjOE7wA5sPOif3yp99212C_i?usp=sharing



 📄 Complete Project Documentation

<div align="center">
<div style="height:700px; overflow-y:auto; border:1px solid #d0d7de; border-radius:8px; padding:10px;">

<img src="./docs/LearnX_Detailed_Overview-images-0.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-1.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-2.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-3.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-4.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-5.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-6.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-7.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-8.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-9.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-10.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-11.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-12.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-13.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-14.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-15.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-16.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-17.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-18.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-19.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-20.jpg" width="100%">
<img src="./docs/LearnX_Detailed_Overview-images-21.jpg" width="100%">
</div>
</div>




## Folder Structure

### Root Directory

```plaintext
project/
|____.gitignore
|____app.py
|____backend
| |____ai
| |____|____assignment_helper.py
| |____|____course_content_assistant.py
| |____|____course_materials
| |____|____|____1
| |____|____|____|____Lecture 8.2 - Divide and Conquer-Closest Pair of Points.pdf
| |____|____|____|____Lecture 8.3 - Divide and Conquer-Integer Multiplication.pdf
| |____|____|____2
| |____|____|____|____Backpropagation.pdf
| |____|____|____|____cs231n_2017_lecture4.pdf
| |____|____|____3
| |____|____|____|____Lecture 8.2 - Divide and Conquer-Closest Pair of Points.pdf
| |____|____|____|____Lecture 8.2 - Divide and Conquer-Closest Pair of Points.pdf:SandBoxSafeFile
| |____|____|____|____Lecture 8.3 - Divide and Conquer-Integer Multiplication.pdf
| |____|____|____|____Lecture 8.3 - Divide and Conquer-Integer Multiplication.pdf:SandBoxSafeFile
| |____|____feedback_review.py
| |____|____grading_assistant.py
| |____|____programming_assistant.py
| |____|____study_planner.py
| |____api.py
| |____celery_factory.py
| |____celery_schedule.py
| |____config.py
| |____create_initial_data.py
| |____mail_service.py
| |____model.py
| |____router.py
| |____tasks.py
|____celerybeat-schedule
|____Dockerfile
|____final_requirements.txt
|____frontend
| |____.DS_Store
| |____app.js
| |____assets
| |____components
| |____index.html
| |____pages
| |____|____Admin_Dashboard.js
| |____|____Course_Content.js
| |____|____Course_Details.js
| |____|____Home.js
| |____|____Instructor_Dashboard.js
| |____|____Instructor_Registration_Page.js
| |____|____Login.js
| |____|____Student_Dashboard.js
| |____|____Student_Registration_Page.js
| |____utils
| |____|____router.js
|____instance
| |____database.sqlite3
|____README.md
|____say_requirements.txt
|____tmp
| |____agent_storage.db
| |____lancedb
| |____|____course_1_docs.lance
| |____|____course_2_docs.lance




