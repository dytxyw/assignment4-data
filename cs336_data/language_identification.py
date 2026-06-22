import fasttext
from typing import Any

def run_identify_language(text: str) -> tuple[Any, float]:
    
    model = fasttext.load_model('lid.176.bin')
    
    prediction = model.predict(text.replace('\n', ' '))# 因为一次只能预测一行文本，所以将换行符替换为空格
    print(prediction)
    
    label = prediction[0][0]
    score = prediction[1][0]
    
    language_code = label.replace('__label__', '')
    return (language_code, score)