# 🤖 AI Outreach Campaign Manager

A sophisticated multi-agent system powered by CrewAI that automates personalized outreach campaigns using AI-driven analysis, content creation, and multi-channel communication.

## 🌟 Features

- **Multi-Agent Architecture**: Leverages CrewAI to orchestrate three specialized AI agents
- **Intelligent Customer Analysis**: AI-powered analysis of customer data and pain points
- **Personalized Content Generation**: Creates tailored phone scripts and email drafts
- **Multi-Channel Outreach**: Executes campaigns via Twilio calls and email
- **Streamlit Web Interface**: User-friendly dashboard for campaign management
- **Azure OpenAI Integration**: Uses Microsoft Azure's GPT-4 for advanced AI capabilities

## 🏗️ Architecture

### Agent System

1. **📊 Customer Data Analyst**
   - Analyzes customer profiles and CRM data
   - Identifies key talking points and product pitches
   - Determines optimal outreach strategies

2. **✍️ Persuasive Copywriter**
   - Creates natural, personalized call scripts
   - Drafts compelling email content
   - Ensures human-like, empathetic communication

3. **📞 Outreach Specialist**
   - Executes phone calls via Twilio API
   - Sends personalized emails
   - Provides execution confirmation reports

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Azure OpenAI Service
- Twilio Account
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/outreach-agent.git
   cd outreach-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Copy `.env.example` to `.env` and configure your credentials:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your credentials:
   ```env
   # Azure OpenAI Credentials
   AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
   AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
   AZURE_OPENAI_API_VERSION="2024-12-01-preview"
   AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4o"
   
   # Required for CrewAI compatibility
   OPENAI_API_KEY="your_azure_openai_api_key"
   
   # Twilio Credentials
   TWILIO_ACCOUNT_SID="your_twilio_account_sid"
   TWILIO_AUTH_TOKEN="your_twilio_auth_token"
   TWILIO_PHONE_NUMBER="+1234567890"
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

The application will open in your web browser at `http://localhost:8501`.

## 📁 Project Structure

```
outreach-agent/
├── app.py                 # Streamlit web application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── README.md            # This file
└── src/
    ├── __init__.py
    ├── agents.py         # CrewAI agent definitions and workflow
    ├── config.py         # Configuration and LLM setup
    └── tools.py          # Custom tools for Twilio and Email
```

## 🔧 Configuration

### Azure OpenAI Setup

1. Create an Azure OpenAI resource in the Azure portal
2. Deploy a GPT-4 model
3. Get your API key, endpoint, and deployment name
4. Add these to your `.env` file

### Twilio Setup

1. Create a Twilio account
2. Get your Account SID and Auth Token
3. Purchase a Twilio phone number
4. Add these credentials to your `.env` file

## 🎯 Usage

1. **Launch the application**: Run `streamlit run app.py`
2. **Enter customer details**: Fill in the customer information form
3. **Launch campaign**: Click the "Launch Campaign 🚀" button
4. **Monitor progress**: Watch as the AI agents analyze, create, and execute the outreach
5. **View results**: Review the execution report and campaign outcomes

## 🛠️ Dependencies

- **streamlit**: Web application framework
- **crewai**: Multi-agent AI orchestration
- **langchain-openai**: Azure OpenAI integration
- **twilio**: SMS and voice communication
- **python-dotenv**: Environment variable management

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and rotate them regularly
- Use environment-specific configurations for production deployments
- Consider using Azure Key Vault for production credential management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/outreach-agent/issues) page
2. Create a new issue with detailed information
3. Join our discussions for community support

## 🌟 Acknowledgments

- [CrewAI](https://crewai.com/) - Multi-agent AI framework
- [Streamlit](https://streamlit.io/) - Web app framework
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) - AI model hosting
- [Twilio](https://www.twilio.com/) - Communication APIs

---

**Built with ❤️ using AI-powered agents**
