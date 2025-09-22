# # from langchain_groq import ChatGroq
# # from app.config.config import GROQ_API_KEY
# # from app.common.logger import get_logger
# # from app.common.custom_exception import CustomException
# #from langchain.llms import HuggingFaceHub
# from langchain_huggingface import HuggingFaceEndpoint
# from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN


# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException


# logger = get_logger(__name__)

# def load_llm(huggingface_repo_id: str = HUGGINGFACE_REPO_ID , hf_token: str = HF_TOKEN):
#     try:
#         logger.info("Loading LLM from HuggingFace")

#         # llm = HuggingFaceEndpoint(
#         #     repo_id=huggingface_repo_id,
#         #     huggingfacehub_api_token=hf_token,
#         #     temperature=0.3,
#         #     max_new_tokens=256,
#         #     return_full_text=False,
#         # )

#         llm = HuggingFaceEndpoint(
#             repo_id="mistralai/Mistral-7B-Instruct-v0.3",
#             task="conversational",    # ✅ Fix here
#             huggingfacehub_api_token=hf_token,
#             temperature=0.3,
#             max_new_tokens=256,
#             return_full_text=False,
#         )


#         logger.info("LLM loaded succesfully...")

#         return llm


#     except Exception as e:
#         error_message = CustomException("Failed to load an LLM from Hugging Face", e)
#         logger.error(str(error_message))
#         return None

# from langchain_groq import ChatGroq
# from app.config.config import GROQ_API_KEY
# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException
# from langchain.llms import HuggingFaceHub

# from langchain_groq import ChatGroq
# from app.config.config import GROQ_API_KEY
# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException
# from langchain.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from app.config.config import HUGGINGFACE_REPO_ID, HF_TOKEN


from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

def load_llm(huggingface_repo_id: str = HUGGINGFACE_REPO_ID , hf_token: str = HF_TOKEN):
    try:
        logger.info("Loading LLM from HuggingFace")

        llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.3",
            huggingfacehub_api_token=hf_token,
            temperature=0.3,
            max_new_tokens=256,
            return_full_text=False,
        )

        # ✅ Wrap endpoint in Chat model so it uses `conversational`
        llm = ChatHuggingFace(llm=llm)

        logger.info("LLM loaded succesfully...")

        return llm

    except Exception as e:
        error_message = CustomException("Failed to load an LLM from Hugging Face", e)
        logger.error(str(error_message))
        return None
