import pyttsx3
import io
import pdfminer.layout
import pdfminer.high_level

class Audio:
    def __init__(self):
        self.book_shelf=["GirlMeetsBoy.pdf","KarlEdwardWagnar.pdf"]

    def read_pdf(self,filename):
        # Initialize text-to-speech engine
        speaker = pyttsx3.init()

        # Open the PDF file in read-binary mode
        with open(filename, 'rb') as file:
            # Create a PDF document object
            document = pdfminer.high_level.extract_text(file)

            for book in self.book_shelf:
                print(book)
            # Print the contents of the PDF document
            speaker.say(document)
            speaker.runAndWait()

# Example usage: read "GirlMeetsBoy.pdf" out loud
read_pdf("GirlMeetsBoy.pdf")
