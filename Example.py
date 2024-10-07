# Training data: (hours studied, exam score)
data = [(1, 50), (3, 65), (5, 80)]

# Initial guess for parameter w
w = 10.0

# Learning rate
learning_rate = 0.01

# Maximum number of iterations (epochs)
epochs = 1000

# Stopping criterion (if the change in w becomes smaller than this)
tolerance = 1e-6

# Training loop: iterating over the data to update w
for epoch in range(epochs):
    w_old = w  # Store the old value of w to check for convergence
    for hours, actual_score in data:
        # Predicted score
        predicted_score = w * hours

        # Calculate error
        error = predicted_score - actual_score

        # Update w based on the error and input hours studied
        w = w - learning_rate * error * hours

    # Check for convergence: if the change in w is smaller than the tolerance, stop
    if abs(w - w_old) < tolerance:
        print(f"Converged after {epoch + 1} epochs")
        break

# Final learned value of w
print(f"Final learned value of w: {w:.6f}")

# Final predictions with the updated w
for hours, actual_score in data:
    predicted_score = w * hours
    error = predicted_score - actual_score
    print(
        f"Hours studied: {hours}, Actual score: {actual_score}, Predicted score: {predicted_score:.2f}, Error: {error:.2f}")
