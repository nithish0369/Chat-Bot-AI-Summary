# Censys Data Summarizer - AI Agent

A full-stack AI-powered application that analyzes and summarizes Censys host data using Perplexity AI. This project demonstrates prompt engineering, AI integration, and user interface design for cybersecurity data analysis.

**AI Tools Used:** Cursor, Claude, Perplexity AI, GitHub Copilot

## 📋 Project Requirements Fulfilled

### ✅ Full-Stack Implementation
- **Backend**: Flask Python application with REST API endpoints
- **Frontend**: Responsive HTML/CSS/JavaScript interface with file upload
- **Integration**: Seamless communication between frontend and backend via JSON API

### ✅ AI Integration
- **LLM Integration**: Perplexity AI (Sonar model) for intelligent data summarization
- **Prompt Engineering**: Sophisticated multi-section prompts for structured output
- **AI Tools**: Leveraged Cursor, Claude, and GitHub Copilot throughout development

### ✅ Summarization Output
- **Structured Reports**: 7-section analysis format (Executive Summary, Metrics, Risk Assessment, etc.)
- **Dual Audience**: Technical and non-technical user support with appropriate language
- **Actionable Insights**: Prioritized recommendations and next steps for security teams

### ✅ User Interface
- **File Upload**: Drag-and-drop JSON file support with validation
- **Real-time Analysis**: Live processing with user feedback
- **Responsive Design**: Works on desktop and mobile devices
- **Professional Output**: Markdown rendering with tables, headings, and formatting

## 🚀 Features

- **AI-Powered Analysis**: Uses Perplexity AI (Sonar model) for intelligent security data summarization
- **File Upload**: Upload JSON files containing Censys host data
- **Interactive UI**: Clean, responsive web interface with real-time analysis
- **Structured Output**: Generates comprehensive reports with executive summaries, metrics, and actionable insights
- **Markdown Rendering**: Professional formatting with tables, headings, and bullet points
- **Dual Audience**: Designed for both technical and non-technical users

## 📋 Project Structure

```
Proj_Deep/
├── app.py                 # Flask backend with Perplexity AI integration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── script.js         # Frontend JavaScript with file upload
│   └── style.css         # Responsive CSS styling
└── README.md             # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Perplexity AI API key

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Proj_Deep.git
cd Proj_Deep
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key
Create a `.env` file in the project root and add your Perplexity API key:
```bash
# Create .env file
echo PERPLEXITY_API_KEY=your-api-key-here > .env
```

Or manually create the `.env` file with:
```
PERPLEXITY_API_KEY=your-api-key-here
```

**Security Note**: The `.env` file is automatically ignored by git to prevent accidental API key commits.

### Step 4: Verify Configuration
Test that your environment is set up correctly:
```bash
python -c "from app import PERPLEXITY_API_KEY; print('✅ API Key loaded:', PERPLEXITY_API_KEY[:20] + '...' if PERPLEXITY_API_KEY else '❌ API Key not found')"
```

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## 🎯 Usage

1. **Open the Application**: Navigate to `http://127.0.0.1:5000`
2. **Upload Data**: Click "Choose File" to upload a JSON file containing Censys host data
3. **Or Paste Data**: Alternatively, paste JSON data directly into the textarea
4. **Generate Summary**: Click "Generate Summary" to analyze the data
5. **View Results**: Review the structured security analysis report

### Sample Data Format
The application accepts Censys host data in the following JSON format. Sample datasets are provided in `sample_data.json` and `sample_test_data.json`:

```json
{
  "hosts": [
    {
      "ip": "192.168.1.1",
      "location": {
        "country": "United States",
        "city": "New York"
      },
      "services": [
        {
          "port": 22,
          "protocol": "SSH",
          "software": [{"product": "openssh", "version": "8.2"}],
          "vulnerabilities": [
            {
              "cve_id": "CVE-2023-1234",
              "severity": "critical",
              "cvss_score": 9.8
            }
          ]
        }
      ],
      "threat_intelligence": {
        "risk_level": "high"
      }
    }
  ]
}
```

**Note**: The project includes sample datasets (`sample_data.json` and `sample_test_data.json`) for testing and demonstration purposes.

## 🧪 Testing Instructions

### Quick Verification
```bash
# Test environment setup
python -c "from app import PERPLEXITY_API_KEY; print('✅ API Key loaded:', PERPLEXITY_API_KEY[:20] + '...' if PERPLEXITY_API_KEY else '❌ API Key not found')"

# Run automated tests
python test_app.py
```

### Functional Correctness Testing
1. **Data Summarization Test**:
   - Upload `sample_data.json` or `sample_test_data.json`
   - Verify all 7 sections appear in output (Executive Summary, Quick Metrics, Risk Assessment, Key Vulnerabilities, Services & Security Issues, Notable Observations, Recommended Actions)
   - Check that metrics are calculated correctly
   - Validate Markdown formatting and table structure

2. **Prompt Engineering Validation**:
   - Test with different risk levels (critical, high, medium)
   - Verify dual-audience language (technical + non-technical explanations)
   - Check structured output format matches requirements
   - Validate executive summary quality and clarity

3. **User Interface Testing**:
   - Test file upload functionality with valid JSON files
   - Test direct data input via textarea
   - Verify real-time processing feedback
   - Check responsive design on different screen sizes

4. **Error Handling Test**:
   - Submit empty data (should show appropriate error)
   - Submit invalid JSON format (should show parsing error)
   - Test with malformed host data structure
   - Test with missing API key (should show configuration error)

5. **AI Integration Testing**:
   - Verify Perplexity AI API calls work correctly
   - Test with various data sizes and complexity
   - Check response time and quality of summaries
   - Validate error handling for API failures

## 🤖 AI Techniques Implemented

### 1. Prompt Engineering
- **Structured Prompts**: Multi-section prompts with clear instructions for 7-section output format
- **Context Awareness**: Prompts adapt to different data types, risk levels, and threat intelligence
- **Output Formatting**: Specific Markdown formatting requirements with tables and bullet points
- **Audience Targeting**: Dual-language approach for technical and non-technical users
- **Length Control**: Optimized prompts for concise yet comprehensive summaries (~250-300 words)
- **Example-Driven**: Includes specific examples for executive summaries and technical explanations

### 2. LLM Integration
- **Perplexity AI API**: Uses Sonar model for real-time analysis and summarization
- **Error Handling**: Robust API error management with graceful fallbacks
- **Response Processing**: JSON parsing and content extraction with validation
- **Token Optimization**: Efficient prompt design to minimize API costs while maximizing quality

### 3. Data Processing
- **JSON Validation**: Client and server-side validation with detailed error messages
- **Metrics Extraction**: Automated calculation of security metrics (hosts, risks, vulnerabilities)
- **Content Analysis**: Intelligent parsing of host data structures and service information
- **Risk Assessment**: Automated risk level classification and threat intelligence processing

### 4. AI Tools Integration
- **Cursor**: AI-powered development environment for code generation and optimization
- **Claude**: Code review, architectural decisions, and prompt engineering assistance
- **GitHub Copilot**: Real-time code suggestions and completion during development
- **Perplexity AI**: Core LLM for data analysis and security summarization

## 📊 Output Format

The AI agent generates reports with:

1. **Executive Summary**: 2-3 sentences in plain language
2. **Quick Metrics**: Host counts, risk levels, vulnerability counts
3. **Overall Risk Assessment**: Concise risk analysis
4. **Key Vulnerabilities**: Detailed CVE table with severity scores
5. **Services and Security Issues**: Per-host analysis table
6. **Notable Observations**: Key findings and patterns
7. **Recommended Next Actions**: Prioritized remediation steps

## 🔧 Development Assumptions

- **Data Format**: Assumes standard Censys JSON structure with hosts array containing IP, location, services, and threat_intelligence fields
- **API Limits**: Perplexity API rate limits and token usage considerations for production deployment
- **Browser Support**: Modern browsers with JavaScript enabled (Chrome, Firefox, Safari, Edge)
- **Network**: Stable internet connection required for Perplexity AI API calls
- **Security**: API key stored securely in `.env` file (not committed to version control)
- **Performance**: Optimized for datasets with 1-50 hosts (scalable architecture for larger datasets)
- **User Experience**: Designed for both technical security analysts and non-technical stakeholders

## 🚀 Future Enhancements

### Short Term (1-2 weeks)
- [x] **Environment Variables**: Move API key to `.env` file ✅
- [ ] **AI Response Accuracy**: Enhanced prompt engineering with more specific instructions and examples
- [ ] **Response Validation**: Post-processing validation to ensure all required sections are present
- [ ] **Input Validation**: Enhanced JSON schema validation with detailed error messages
- [ ] **Error Recovery**: Better error messages and retry mechanisms for API failures
- [ ] **Loading States**: Progress indicators and status updates for long analyses
- [ ] **Export Features**: PDF/CSV export of reports for sharing and documentation
- [ ] **Data Visualization**: Charts and graphs for risk metrics and vulnerability trends

### Medium Term (1-2 months)
- [ ] **Advanced AI Accuracy**: Multi-model approach with response comparison and validation
- [ ] **Context-Aware Analysis**: Enhanced prompts that adapt based on data complexity and threat levels
- [ ] **Response Quality Scoring**: Automated quality metrics for generated summaries
- [ ] **Feedback Loop**: User feedback collection to improve AI responses over time
- [ ] **Authentication**: User login and session management for multi-user environments
- [ ] **Database Integration**: Store analysis history, results, and user preferences
- [ ] **Batch Processing**: Analyze multiple datasets simultaneously with queue management
- [ ] **Custom Prompts**: User-defined analysis templates and prompt customization
- [ ] **API Rate Limiting**: Implement proper rate limiting and queuing for production use
- [ ] **Advanced Filtering**: Filter and search capabilities for large datasets

### Long Term (3-6 months)
- [ ] **AI Model Fine-tuning**: Custom fine-tuned models specifically for cybersecurity data analysis
- [ ] **Ensemble AI Approach**: Multiple AI models working together for higher accuracy
- [ ] **Domain-Specific Training**: AI models trained on cybersecurity datasets and threat intelligence
- [ ] **Machine Learning**: Custom models for threat detection and risk prediction
- [ ] **Real-time Monitoring**: Live data feed integration with Censys API
- [ ] **Collaboration**: Team sharing, commenting, and collaborative analysis features
- [ ] **Advanced Analytics**: Trend analysis, reporting dashboards, and historical comparisons
- [ ] **Integration**: Connect with other security tools (SIEM, SOAR, ticketing systems)
- [ ] **Mobile App**: Native mobile application for on-the-go security analysis

### AI Accuracy & Quality Improvements
- [ ] **Prompt Engineering Optimization**: A/B testing different prompt structures for better accuracy
- [ ] **Response Consistency**: Implement checks to ensure consistent output format and quality
- [ ] **Error Detection**: Automated detection of incomplete or inaccurate AI responses
- [ ] **Context Enhancement**: Better data preprocessing to provide more context to AI models
- [ ] **Validation Rules**: Business logic validation for AI-generated security assessments
- [ ] **Human-in-the-Loop**: Optional human review and correction of AI responses
- [ ] **Accuracy Metrics**: Track and measure AI response accuracy over time
- [ ] **Continuous Learning**: System that learns from corrections and improves over time

### Technical Improvements
- [ ] **Unit Tests**: Comprehensive test coverage with pytest and automated testing
- [ ] **Docker**: Containerization for easy deployment and scaling
- [ ] **CI/CD**: Automated testing, deployment, and continuous integration
- [ ] **Performance**: Caching, optimization, and horizontal scaling capabilities
- [ ] **Security**: Enhanced input sanitization, API security, and audit logging
- [ ] **Monitoring**: Application performance monitoring and alerting systems

## 🏗️ Architecture

```
Frontend (HTML/CSS/JS)
    ↓ HTTP Requests
Flask Backend (Python)
    ↓ API Calls
Perplexity AI (LLM)
    ↓ Analysis
Structured Report (Markdown)
```

## 📝 API Documentation

### POST /summarize
Analyzes Censys host data and returns structured summary.

**Request Body:**
```json
{
  "hosts": [
    {
      "ip": "string",
      "location": {...},
      "services": [...],
      "threat_intelligence": {...}
    }
  ]
}
```

**Response:**
```json
{
  "metrics": {
    "total_hosts": 3,
    "critical_risk": 1,
    "high_risk": 2,
    "services_count": 11,
    "unique_vulnerabilities": 3,
    "countries": ["US", "CN"]
  },
  "summary": "Markdown formatted analysis...",
  "hosts_count": 3
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues:
- Create an issue in the repository
- Contact: [your-email@example.com]

## 🔒 Security Improvements

### Recent Updates (Latest)
- ✅ **Environment Variables**: API keys now stored securely in `.env` file
- ✅ **Git Security**: `.env` file automatically ignored by git
- ✅ **Runtime Loading**: API keys loaded securely at application startup
- ✅ **No Hardcoded Secrets**: Removed all hardcoded API keys from source code

### Security Best Practices Implemented
1. **Environment Variable Management**: Using `python-dotenv` for secure configuration
2. **Git Ignore**: Sensitive files excluded from version control
3. **Runtime Validation**: API key validation on application startup
4. **Error Handling**: Graceful handling of missing environment variables

---

**Note**: This project was developed as a take-home assignment for an AI Engineer intern position, demonstrating full-stack development skills and AI integration capabilities.
