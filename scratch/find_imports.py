
import sys

def check_import(name, path):
    try:
        exec(f"from {path} import {name}")
        print(f"SUCCESS: {name} found in {path}")
        return True
    except Exception as e:
        # print(f"DEBUG: Failed {name} from {path}: {e}")
        return False

print("Python version:", sys.version)

classes_to_find = {
    "ConversationalRetrievalChain": ["langchain.chains", "langchain_community.chains", "langchain_classic.chains"],
    "ConversationBufferMemory": ["langchain.memory", "langchain_community.memory", "langchain_classic.memory", "langchain.schema"],
}

for name, paths in classes_to_find.items():
    found = False
    for path in paths:
        if check_import(name, path):
            found = True
            break
    if not found:
        print(f"FAILED: Could not find {name} anywhere.")
