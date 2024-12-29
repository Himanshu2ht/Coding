import numpy as np

# Function to encode a message using a nonsingular matrix
def encode_message(message, key_matrix):
    # Convert message into numbers (ASCII values)
    vector = [ord(char) for char in message]

    # Padding if the length is not divisible by the number of columns in the key_matrix
    n = key_matrix.shape[1]
    while len(vector) % n != 0:
        vector.append(ord(' '))  # Pad with ASCII for space

    # Reshape vector into matrix form
    vector_matrix = np.array(vector).reshape(-1, n)

    # Encode the message
    encoded = np.dot(vector_matrix, key_matrix)
    return encoded

# Function to decode a message using the inverse of the key matrix
def decode_message(encoded_matrix, key_matrix):
    # Calculate the inverse of the key matrix
    key_inverse = np.linalg.inv(key_matrix)

    # Decode the matrix
    decoded_matrix = np.dot(encoded_matrix, key_inverse)

    # Flatten and round to nearest integer (ASCII values)
    decoded_vector = decoded_matrix.flatten().round().astype(int)

    # Convert back to characters
    decoded_message = ''.join(chr(val) for val in decoded_vector)
    return decoded_message

# Example message and key matrix
message = "Linear Algebra is fun"
key_matrix = np.array([[2, 1],
                       [3, 2]])  # A nonsingular matrix

# Encoding
encoded_message = encode_message(message, key_matrix)
print("Encoded message:", encoded_message)

# Decoding
decoded_message = decode_message(encoded_message, key_matrix)
print("Decoded message:", decoded_message)
