from openai import OpenAI
import os


client = OpenAI(api_key='YOUR_API_KEY')


def split_text(text, max_length=4000):
    # splite text to avoid length larger than max_length of tokens
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]


def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}. Keep the form of text as code. No need to show it as code view. (Translate ウズスタジオ as UZU STUDIO):\n\n{text}"
    response = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=4000,
    temperature=0.3)
    translated_text = response.choices[0].message.content
    return translated_text


# read file and write the translation in the same file
def translate_markdown_file(file_path, source_language, target_language):
    # read original file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # splite text to avoid crossing the limmitation of token
    segments = split_text(content)
    translated_segments = []

    # translate every segment
    for segment in segments:
        translated_segments.append(translate_text(segment, source_language, target_language))

    # merge all segment
    translated_content = "\n".join(translated_segments)

    # write the translation into the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)


def translate_markdown_in_folder(folder_path, source_language, target_language):
    
    # walk through all files
    for root, _, files in os.walk(folder_path):
        for file in files:
            # make sure the file is .md
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Translating file: {file_path}")
                translate_markdown_file(file_path, source_language, target_language)


# example

file_path = 'YOUR_PATH_TO_THE_FILE'

# translate for a folder
translate_markdown_in_folder(file_path, source_language='Japanese', target_language='Traditional Chinese')

# translate for a single .md file
translate_markdown_file(file_path, source_language='Japanese', target_language='Traditional Chinese')