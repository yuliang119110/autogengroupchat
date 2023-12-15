import sys
import json
import autogen
import os
from autogen import config_list_from_json
from autogen import AssistantAgent, UserProxyAgent
import logging

# 配置日志模块
logging.basicConfig(level=logging.INFO)

# Function to run the query
def run_query(programming_problem, api_key):
    config_list = [
        {
            'model': 'gpt-4-1106-preview',
            'api_key': api_key,
            'api_base': api_base,
        },
        {
            'model': 'gpt-4-1106-preview',
            'api_key': api_key,
            'api_base': api_base,
        },
        {
            'model': 'gpt-4-1106-preview',
            'api_key': api_key,
            'api_base': api_base,
        },
    ]
    
    pm_llm_config = {"config_list": config_list}

    llm_config = {"config_list": config_list}
    
    code_llm_config = {"config_list": config_list}
    
    # autogen.ChatCompletion.start_logging()

    # Create user proxy agent, coder, product manager
    user_proxy = autogen.UserProxyAgent(
        name="User_proxy",
        system_message="You are the demand side for market size research results, assigning corresponding tasks to different roles [Market_research_agent, Industry_analysis_agent, Competition_analysis_agent,Customer_needs_analysis_agent,Macroeconomic_analysis_agent,Technology_analysis_agent,Data_analysis_agent,Market_size_forecasting_agent,Market_size_simulation_agent,Market_size_reporting_agent]to complete market size reports",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat","use_docker":"python:3"},
        human_input_mode="NEVER",
    )
    Market_research_agent = autogen.AssistantAgent(
        name="Market_research_agent",
        system_message="You will collect data such as industry reports, market research, and expert opinions. You will strive to gather accurate and complete data according to instructions. Your expertise and experience include market research and data analysis.",

        llm_config=llm_config,
    )
    Industry_analysis_agent = autogen.AssistantAgent(
        name="Industry_analysis_agent",
        system_message="You will analyze data such as market historical data, market trends, and competitive landscape. You will identify key factors of market size based on this data and provide forecasts. Your expertise and experience include industry analysis and data analysis.",
        llm_config=code_llm_config,
    )
    Competition_analysis_agent = autogen.AssistantAgent(
        name="Competition_analysis_agent",
        system_message="You will analyze data such as competitors' market share, sales volume, and growth rates. You will understand the major competitors in the market and analyze their strengths and weaknesses. Your expertise and experience include competitive analysis and data analysis.",
        llm_config=pm_llm_config,
    )
    Customer_needs_analysis_agent = autogen.AssistantAgent(
        name="Customer_needs_analysis_agent",
        system_message="You will analyze data such as customer needs, behavior, and preferences. You will study the demand for AI technology among customers and understand the needs of different industries and businesses of various sizes. Your expertise and experience include customer needs analysis and data analysis",
        llm_config=pm_llm_config,
    )
    Macroeconomic_analysis_agent = autogen.AssistantAgent(
        name="Macroeconomic_analysis_agent",
        system_message="You will analyze data such as economic growth, industry investment, and government policies. You will consider how factors like economic growth, industry investment, and government policies affect the AI market. Your expertise and experience include macroeconomic analysis and data analysis",
        llm_config=pm_llm_config,
    )
    Technology_analysis_agent = autogen.AssistantAgent(
        name="Technology_analysis_agent",
        system_message="You will analyze data related to technological advancements and the emergence of new technologies. You will assess how technological progress drives market growth and how the advent of new technologies impacts the existing market structure. Your expertise and experience include technology analysis and data analysis.",
        llm_config=pm_llm_config,
    )
    Data_analysis_agent = autogen.AssistantAgent(
        name="Data_analysis_agent",
        system_message="You will analyze various types of data, including market data, competitive data, customer data, macroeconomic data, and technological data. Based on the collected data and analysis results, you will develop a market size forecasting model. Your expertise and experience include data analysis, machine learning, and statistics.",
        llm_config=pm_llm_config,
    )
    Market_size_forecasting_agent = autogen.AssistantAgent(
        name="Market_size_forecasting_agent",
        system_message="You will utilize models such as time series analysis, regression analysis, and machine learning to build a market size forecast model. Based on collected data and analysis results, you will select the appropriate model and perform parameter estimation. Your expertise and experience are in data analysis, machine learning, and statistics. Specifically, you will follow these steps to build a market size forecasting model:",
        llm_config=pm_llm_config,
    )
    Market_size_simulation_agent = autogen.AssistantAgent(
        name="Market_size_simulation_agent",
        system_message="You will conduct simulations for market size forecasting models using software tools such as Excel, R language, and Python. You will perform simulation calculations based on the model's parameters and the scenario being simulated. Your expertise and experience are in data analysis, machine learning, and statistics.",
        llm_config=pm_llm_config,
    )
    Market_size_reporting_agent = autogen.AssistantAgent(
        name="Market_size_reporting_agent",
        system_message="You will generate market size reports that may include market size estimation reports with estimated values, growth trends, and driving factors; market competition analysis reports with competitor analysis and competitive landscape; and market opportunity analysis reports with identification of market opportunities and market potential. You will endeavor to produce accurate and useful reports according to your instructions. Your expertise and experience include report writing, report design, and report production.",
        llm_config=pm_llm_config,
    )

    # Create groupchat
    groupchat = autogen.GroupChat(
        agents=[user_proxy, Market_research_agent, Industry_analysis_agent, Competition_analysis_agent,Customer_needs_analysis_agent,Macroeconomic_analysis_agent,Technology_analysis_agent,Data_analysis_agent,Market_size_forecasting_agent,Market_size_simulation_agent,Market_size_reporting_agent], messages=[])
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)


    return user_proxy.initiate_chat(manager, message=programming_problem)


if __name__ == "__main__":
    input_data = json.loads(sys.stdin.read())
    programming_problem = input_data['programming_problem']
    # api_key = os.getenv("OPENAI_API_KEY")
    api_key = "sk-6rgIEYD7ZpfFcBGqF68497F3357047B2AaEc84E3B52554E0"
    api_base = "https://api.aiwe.io/v1"
    base_url = "https://api.aiwe.io/v1"
    result = run_query(programming_problem, api_key)
    logging.info("run_query result: %s", result)
