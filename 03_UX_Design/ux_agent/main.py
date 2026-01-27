import sys
import argparse
from ux_agent import UXAgent

def main():
    parser = argparse.ArgumentParser(description="AI-Augmented UX Agent")
    parser.add_argument('input_file', help="Path to input text file (Story or Design Description)")
    parser.add_argument('--mode', choices=['flow', 'review', 'simulate'], default='flow', help="Operation mode")
    
    args = parser.parse_args()

    agent = UXAgent()
    agent.run(args.input_file, mode=args.mode)

if __name__ == "__main__":
    main()
