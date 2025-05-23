#!/usr/bin/env python3

import argparse
import subprocess
import sys
import time


def run_llm(model, prompt, conversation_id=None):
    """Run the llm command with the given model and prompt."""
    cmd = ["llm", "-m", model]
    
    if conversation_id:
        cmd.extend(["-c", conversation_id])
    
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running llm with model {model}: {e}", file=sys.stderr)
        print(f"stderr: {e.stderr}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Have two LLMs chat with each other"
    )
    parser.add_argument(
        "--model1", "-m1",
        default="claude-4-sonnet",
        help="Model for the first LLM (default: claude-4-sonnet)"
    )
    parser.add_argument(
        "--model2", "-m2",
        default="claude-4-sonnet", 
        help="Model for the second LLM (default: claude-4-sonnet)"
    )
    parser.add_argument(
        "--topic", "-t",
        default="Tell me an interesting fact about space.",
        help="Initial topic/prompt to start the conversation"
    )
    parser.add_argument(
        "--rounds", "-r",
        type=int,
        default=5,
        help="Number of conversation rounds (default: 5)"
    )
    parser.add_argument(
        "--delay", "-d",
        type=float,
        default=1.0,
        help="Delay between responses in seconds (default: 1.0)"
    )
    
    args = parser.parse_args()
    
    print(f"🤖 Starting conversation between {args.model1} and {args.model2}")
    print(f"📝 Topic: {args.topic}")
    print(f"🔄 Rounds: {args.rounds}")
    print("=" * 60)
    
    # Start the conversation
    current_prompt = args.topic
    
    for round_num in range(args.rounds):
        # Model 1's turn
        print(f"\n🤖 {args.model1} (Round {round_num + 1}):")
        print("-" * 40)
        
        response1 = run_llm(args.model1, current_prompt)
        if response1 is None:
            print("❌ Failed to get response from model 1")
            break
            
        print(response1)
        
        time.sleep(args.delay)
        
        # Model 2's turn
        print(f"\n🤖 {args.model2} (Round {round_num + 1}):")
        print("-" * 40)
        
        # Use model 1's response as the prompt for model 2
        response2 = run_llm(args.model2, response1)
        if response2 is None:
            print("❌ Failed to get response from model 2")
            break
            
        print(response2)
        
        # Use model 2's response as the prompt for the next round
        current_prompt = response2
        
        time.sleep(args.delay)
    
    print("\n" + "=" * 60)
    print("🏁 Conversation ended")


if __name__ == "__main__":
    main()