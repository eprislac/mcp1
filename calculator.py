#basic import
from mcp.server.fastmcp import FastMCP
import math

# instatntiate an MCP server client
mcp = FastMCP("Hello World")

# define tools

# addtion tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return int(a * b)

# division tool
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Calculate the square root of a number"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return float(math.sqrt(a))

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Calculate the cube root of a number"""
    return float(a ** (1/3))

# power tool
@mcp.tool()
def power(a: int, b: int) -> float:
    """Calculate a raised to the power of b"""
    return float(math.pow(a, b))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """Calculate the factorial of a number"""
    if a < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    return int(math.factorial(a))

# logarithm tool
@mcp.tool()
def log(a: int, base: int = 10) -> float:
    """Calculate the logarithm of a number with given base"""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 1:
        raise ValueError("Logarithm base must be greater than 1")
    return float(math.log(a, base))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """Calculate the remainder of a divided by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return int(a % b)

# absolute value tool
@mcp.tool()
def abs(a: int) -> int:
    """Calculate the absolute value of a number"""
    return int(abs(a))

# sine tool
@mcp.tool()
def sin(a: int) -> float:
    """Calculate the sine of an angle in radians"""
    return float(math.sin(a))

# cosine tool
@mcp.tool()
def cos(a: int) -> float:
    """Calculate the cosine of an angle in radians"""
    return float(math.cos(a))

# tangent tool
@mcp.tool()
def tan(a: int) -> float:
    """Calculate the tangent of an angle in radians"""
    return float(math.tan(a))

# define resources
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting message"""
    return f"Hello, { name }! Welcome to the Calculator MCP Server."

# execute and return the stdio output
if __name__ == "__main__":
    mcp.run(transport="stdio")
