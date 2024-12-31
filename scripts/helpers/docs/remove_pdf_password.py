import os
from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_file, output_file, password):
    try:
        # Open the encrypted PDF
        with open(input_file, 'rb') as file:
            reader = PdfReader(file)

            # Check if the PDF is encrypted
            if reader.is_encrypted:
                # Try to decrypt the PDF with the provided password
                if reader.decrypt(password):
                    # Create a PdfWriter object
                    writer = PdfWriter()

                    # Add all pages to the writer
                    for page in reader.pages:
                        writer.add_page(page)

                    # Write the decrypted PDF to a new file
                    with open(output_file, 'wb') as output_pdf:
                        writer.write(output_pdf)

                    print(f"Password removed: {input_file} -> {output_file}")
                else:
                    print(f"Failed to decrypt {input_file}. Incorrect password.")
            else:
                print(f"{input_file} is not encrypted.")
                os.rename(input_file, output_file)

    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}")

def main():
    # Get the working directory from the user
    working_directory = input("Enter the directory containing the PDF files (leave blank for current directory): ").strip()

    # Use the current directory if no directory is provided
    if not working_directory:
        working_directory = os.getcwd()

    # Validate the directory
    if not os.path.isdir(working_directory):
        print(f"The directory '{working_directory}' does not exist.")
        return

    # Get the password from the user
    password = input("Enter the password for the PDF files: ")

    # Create a new directory for decrypted files
    decrypted_dir = os.path.join(working_directory, 'decrypted')
    os.makedirs(decrypted_dir, exist_ok=True)

    # Get all PDF files in the specified directory
    pdf_files = [f for f in os.listdir(working_directory) if f.lower().endswith('.pdf')]

    # Process each PDF file
    for pdf_file in pdf_files:
        # Define the full path for the input and output files
        input_file = os.path.join(working_directory, pdf_file)
        output_file = os.path.join(decrypted_dir, pdf_file)

        # Remove the password protection
        remove_pdf_password(input_file, output_file, password)

if __name__ == "__main__":
    main()