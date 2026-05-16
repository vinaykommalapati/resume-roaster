import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def roast_resume(resume_text):
    print("\n🔥 Roasting your resume...\n")

    roast_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a brutally honest, witty comedian who roasts resumes.
                Your roast should be funny, sharp, and savage — but not mean-spirited.
                Point out weak action verbs, vague descriptions, obvious skills like 'Microsoft Word',
                generic objectives, and anything that makes the resume look amateur.
                Keep the roast to 5-7 punchy lines. Be creative and funny!"""
            },
            {
                "role": "user",
                "content": f"Roast this resume:\n\n{resume_text}"
            }
        ],
        max_tokens=1024
    )

    roast = roast_response.choices[0].message.content
    print("🎤 THE ROAST:")
    print("-" * 50)
    print(roast)
    print("-" * 50)

    print("\n💡 Okay, jokes aside. Here's how to actually fix it:\n")

    fix_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a professional resume coach.
                After a roast, give 5 specific, actionable improvements for the resume.
                Be direct and practical. Format as numbered list."""
            },
            {
                "role": "user",
                "content": f"Give 5 specific improvements for this resume:\n\n{resume_text}"
            }
        ],
        max_tokens=1024
    )

    fixes = fix_response.choices[0].message.content
    print("✅ TOP 5 FIXES:")
    print("-" * 50)
    print(fixes)
    print("-" * 50)


def main():
    print("=" * 50)
    print("   AI Resume Roaster 🔥")
    print("   Built by Vinay Kommalapati")
    print("=" * 50)
    print("\nPaste your resume below.")
    print("When done, type 'DONE' on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)

    resume_text = "\n".join(lines)

    if not resume_text.strip():
        print("❌ No resume text entered. Please try again.")
        return

    roast_resume(resume_text)

    print("\nWant to roast another resume? Restart the app!")
    print("\nGoodbye! Go fix that resume! 💪\n")


if __name__ == "__main__":
    main()
