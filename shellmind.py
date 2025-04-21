from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import os
import llama

console = Console()

# Initialize the TinyLlama model
def load_tinyllama():
    model_path = "/path/to/tinyLlama.bin"  # Set path to the model file
    model = llama.load_model(model_path)
    return model

# Function to generate LLM response for queries
def generate_llm_response(query):
    model = load_tinyllama()
    response = model.generate(query)
    return response

def banner():
    console.print(Panel.fit("[bold green]\U0001F9E0 ShellMind - Your Hacker AI Assistant[/bold green]\n[cyan]By Technifai[/cyan]", border_style="magenta"))

def show_menu():
    console.print("\n[bold cyan]Choose an option:[/bold cyan]")
    console.print("[1] Generate Payload")
    console.print("[2] Suggest Tools")
    console.print("[3] Lookup CVE (offline demo)")
    console.print("[4] Generate Bash Script")
    console.print("[5] Run Nmap Scan")
    console.print("[6] Run Hydra Command Generator")
    console.print("[7] Show User Info")
    console.print("[8] Query LLM (Offline)")
    console.print("[9] Exit")

def query_llm():
    query = Prompt.ask("What do you want to ask the AI?", default="Which tool to use for ethical WiFi hacking?")
    response = generate_llm_response(query)
    console.print(f"\n[bold green]AI Response:[/bold green] {response}", style="yellow")

def main():
    banner()
    while True:
        show_menu()
        choice = Prompt.ask("\n[?] Your choice", choices=[str(i) for i in range(1, 10)])

        if choice == "1":
            generate_payload()
        elif choice == "2":
            suggest_tools()
        elif choice == "3":
            lookup_cve()
        elif choice == "4":
            bash_script_generator()
        elif choice == "5":
            run_nmap()
        elif choice == "6":
            run_hydra_generator()
        elif choice == "7":
            show_user_info()
        elif choice == "8":
            query_llm()  # New LLM Query option
        elif choice == "9":
            confirm = Prompt.ask("Exit ShellMind? (y/n)", default="y")
            if confirm.lower() == "y":
                console.print("Goodbye, hacker \U0001F9E0", style="bold red")
                break

if __name__ == "__main__":
    main()
