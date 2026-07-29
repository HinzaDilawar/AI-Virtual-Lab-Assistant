from groq import Groq

GROQ_API_KEY = "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"



def _get_client():

    return Groq(api_key=GROQ_API_KEY)



def chat_with_ai(question):

    try:

        client = _get_client()

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {

                    "role": "system",

                    "content": """You are a helpful AI assistant for a virtual computer lab.

Answer ANY question — Python, C++, JavaScript, algorithms, debugging, or general knowledge.

Keep answers clear, friendly, and concise. Use simple examples when explaining concepts."""

                },

                {

                    "role": "user",

                    "content": question

                }

            ],

            max_tokens=800

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ AI Error: {str(e)}"



def analyze_code(lang, code):

    try:

        client = _get_client()

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {

                    "role": "user",

                    "content": f"Analyze this {lang} code (3 sentences max): what it does, any bugs, one improvement tip.\n\nCode:\n```{lang}\n{code}\n```"

                }

            ],

            max_tokens=500

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ AI feedback unavailable: {str(e)}"



def get_hint(lang, code):

    try:

        client = _get_client()

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {

                    "role": "user",

                    "content": f"Give a short helpful hint (2-3 sentences) for this {lang} code:\n```{lang}\n{code}\n```"

                }

            ],

            max_tokens=300

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ Hint unavailable: {str(e)}"





