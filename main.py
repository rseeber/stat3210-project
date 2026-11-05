class Details:
    def __init__(self):
        self.user1 = ""
        self.user2 = ""
        self.rules = ""
        self.report_note = ""

        self.msg1 = ""   # Context
        self.msg2 = ""   # reply from reporter
        #self.msg3 = ""   # reported message

def getReport(details: Details):
    report_template = f"""\
You are a chatbot performing social media moderation pre-screenings. The rules for this community are as follows:
=== Rules ===
{details.rules}

=== Report ===
The following report was received.
Reporter: {details.user1}
Note by {details.user1}:
\"\"\"
{details.report_note}
\"\"\"

=== Thread ===
[1] {details.user1} (reporter):
\"\"\"
{details.msg1}
\"\"\"

[2] {details.user2} [REPORTED POST]
\"\"\"
{details.msg2}
\"\"\"

=== Analysis ===

It is now your job to decide if this user was rightfully reported, or if this report can be ignored. You may reply with “Continue” if this report is correct, and it will be passed up to a human moderator to make the final call on, or “Ignore” to automatically dismiss the report without a human needing to waste energy reviewing it. Your reply is going to be processed programmatically, so please reply ONLY with “Continue” or “Ignore” on the first line. You may include additional notes if necessary on the subsequent line.

"""
    return report_template


def main():
    d = Details()
    d.user1 = "Alice"
    d.user2 = "Bob"
    d.rules = """\
1. Be respectful
2. No spam
3. Don't make me add new rules\
"""
    d.report_note = "Obvious spam"

    d.msg1 = "Boyfriend taking me to the mall later today!!"
    d.msg2 = """\
Make sure to sign up for RAID SHADOW LEGENDS!!

And sign up for NordVPN!!"""

    # save to file
    txt = getReport(d)
    with open("output.txt", "w") as f:
        f.write(txt)
    print("Template written to output.txt")

if __name__ == "__main__":
    main()