import argparse
import os
import time
from threading import Thread

# CLI Tool Integrator Class
class RealTimeCLIToolIntegrator:
    def __init__(self):
        self.tools = {}

    def add_tool(self, tool_name, command):
        self.tools[tool_name] = command

    def remove_tool(self, tool_name):
        if tool_name in self.tools:
            del self.tools[tool_name]

    def list_tools(self):
        for tool_name, command in self.tools.items():
            print(f"{tool_name}: {command}")

    def run_tool(self, tool_name):
        if tool_name in self.tools:
            os.system(self.tools[tool_name])
        else:
            print(f"Tool '{tool_name}' not found.")

    def start_realtime_integrator(self):
        while True:
            try:
                user_input = input("Enter a tool to run (or 'list' to list tools, 'add' to add a tool, 'remove' to remove a tool, 'exit' to exit): ")
                if user_input == 'list':
                    self.list_tools()
                elif user_input == 'add':
                    tool_name = input("Enter the tool name: ")
                    command = input("Enter the command: ")
                    self.add_tool(tool_name, command)
                elif user_input == 'remove':
                    tool_name = input("Enter the tool name: ")
                    self.remove_tool(tool_name)
                elif user_input == 'exit':
                    break
                else:
                    self.run_tool(user_input)
            except KeyboardInterrupt:
                print("\nExiting...")
                break

# Main function
def main():
    integrator = RealTimeCLIToolIntegrator()
    integrator.start_realtime_integrator()

if __name__ == "__main__":
    main()