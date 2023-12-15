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
        system_message="A human admin who will give the idea and run the code provided by Coder.",
        code_execution_config={"last_n_messages": 2, "work_dir": "groupchat","use_docker":"python:3"},
        human_input_mode="NEVER",
    )
    coder = autogen.AssistantAgent(
        name="Coder",
        llm_config=llm_config,
    )
    code_assistant = autogen.AssistantAgent(
        name="Code_assistant",
        system_message="You will analyze code, test the code, and provide recomendations",
        llm_config=code_llm_config,
    )
    pm = autogen.AssistantAgent(
        name="product_manager",
        system_message="You will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future conversations or error fixing",
        llm_config=pm_llm_config,
    )

    # Create groupchat
    groupchat = autogen.GroupChat(
        agents=[user_proxy, coder, code_assistant, pm], messages=[])
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
