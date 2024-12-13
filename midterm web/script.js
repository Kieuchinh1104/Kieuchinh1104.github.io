<script>
        function calculate(operation) {
            // Get the values from the input fields
            const num1 = document.getElementById("num1").value;
            const num2 = document.getElementById("num2").value;

            // Validate that inputs are not empty
            if (num1 === "" || num2 === "") {
                document.getElementById("result").innerText = "Please enter both numbers.";
                return;
            }

            // Convert the input strings to numbers
            const number1 = parseFloat(num1);
            const number2 = parseFloat(num2);

            let result;

            // Perform the calculation based on the operation
            switch (operation) {
                case '+':
                    result = number1 + number2;
                    break;
                case '-':
                    result = number1 - number2;
                    break;
                
                case '/':
                    if (number2 === 0) {
                        document.getElementById("result").innerText = "Cannot divide by 0.";
                        return;
                    }
                    result = number1 / number2;
                    break;
                
                case '*':
                    result = number1 * number2;
                    break;
                default:
                    result = "Invalid operation";
            }

            // Display the result
            document.getElementById("result").innerText = "Result: " + result;
        }
    </script>
</body>
</html>