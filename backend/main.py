#!/usr/bin/env python3
"""
Main entry point for the AI Assistant.
Handles both content ingestion and chat modes.
"""

import sys
import argparse
from ingest_local_docs import ingest_local_docs
from chat_gemini import query_qdrant, format_response


def run_chat_interface():
    """Run the command-line chat interface."""
    print("Physical AI & Humanoid Robotics Curriculum Assistant")
    print("Type 'quit' or 'exit' to stop the chat.\n")
    
    while True:
        try:
            query = input("You: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not query:
                continue
            
            print("Searching for relevant information...")
            search_results = query_qdrant(query)
            response = format_response(query, search_results)
            
            print(f"Assistant: {response}\n")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="AI Assistant for Physical AI & Humanoid Robotics Curriculum")
    parser.add_argument("mode", choices=["ingest", "chat"], help="Operation mode: ingest or chat")
    
    args = parser.parse_args()
    
    if args.mode == "ingest":
        print("Starting content ingestion process...")
        ingest_local_docs()
    elif args.mode == "chat":
        print("Starting chat interface...")
        run_chat_interface()


if __name__ == "__main__":
    main()