import re

def extract_yt_term(command):
    # Normalize to lowercase
    command = command.lower()

    # Optional words before 'play', like 'please', 'can you', 'quickly', etc.
    command = re.sub(r'\b(please|can you|could you|quickly|kindly)\b', '', command)

    # Match different ways of saying "play X on/in/from/at youtube"
    pattern = r'play\s+(.*?)\s+(on|in|from|at)\s+youtube'
    match = re.search(pattern, command)

    if match:
        return match.group(1).strip()
    
    # Fallback: if only 'play' and 'youtube' are present
    if "play" in command and "youtube" in command:
        command = command.replace("play", "").replace("youtube", "")
        return command.strip()

    return None
def remove_words(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string=' '.join(filtered_words)
    return result_string
