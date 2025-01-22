from cohere import ClientV2


class CohereClient:
    def __init__(self,
                 api_key,
                 model="command-r-plus-08-2024",
                 max_tokens=500,
                 temperature=0.7
                 ):
        self.client = ClientV2(api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.conversation_history = []

    def build_prompt(self, user_input, context=None):
        context_str = f"{context}\n\n" if context else ""
        return (
            f"{context_str}"
            f"Question: {user_input}\n"
            f"Provide straight to the point response except when told "
            f"to elaborate using available metrics and historical data"
        )

    def chat(self, user_input, context=None):
        try:
            system_message = """
            You are an intelligent system specialized in human chat interaction,
            interpersonal interactions and can guide on complex ideas.
            Consider all available metrics, trends, and patterns in your analysis.
            Make connections between different points to provide deeper insights.
            Support your analysis with specific numbers and trends.
            """

            full_prompt = self.build_prompt(user_input, context)

            response = self.client.chat(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": full_prompt}
                ]
            )

            # Extract response text
            assistant_reply = response.message.content[0].text

            # Update conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": assistant_reply})

            # Maintain history within length
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]

            return assistant_reply

        except Exception as e:
            return f"Error generating response: {str(e)}"
