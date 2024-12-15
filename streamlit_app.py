import streamlit as st
import re

class TextFormatter:
    """Minimal text formatter for demonstration purposes."""
    def format_text(self, input_string: str) -> str:
        """Format text if needed. For simplicity, no advanced logic here."""
        return input_string.strip().replace(".", "")

class LinkBuilder:
    """Builds campaign links based on given parameters."""
    def build(self, category: str, topic: str, mov: str = None, optional: str = None) -> str:
        parts = [category, topic]

        if category == "Promotion":
            parts.append(mov)

        if optional:
            parts.append(optional)

        # Filter out any None values and join with underscore
        parts = [p for p in parts if p]
        return "_".join(parts)

def main():
    text_formatter = TextFormatter()
    link_builder = LinkBuilder()

    # Hard-coded categories
    categories = ["Campaign", "Promotion"]
    category = st.selectbox("Select a campaign `type`", categories, index=0)

    topic = st.text_input("Specify `topic`")
    topic = text_formatter.format_text(topic)

    mov = None
    if category == "Promotion":
        mov = st.text_input("Specify the `Minimum Order Value`")
        mov = text_formatter.format_text(mov)

    optional = st.text_input("If the campaign needs to be tracked separately, specify any `additional qualifier`")
    optional = text_formatter.format_text(optional)

    if st.button("Build Link"):
        link = link_builder.build(category, topic, mov, optional)
        st.code(link)

if __name__ == "__main__":
    main()
