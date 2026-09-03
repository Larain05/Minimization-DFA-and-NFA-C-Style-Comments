using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter input string: ");
        string input = Console.ReadLine();

        if (IsAccepted(input))
        {
            Console.WriteLine("Accepted");
        }
        else
        {
            Console.WriteLine("Rejected");
        }
    }

    static bool IsAccepted(string input)
    {
        //Start at q0
        HashSet<string> currentStates = new HashSet<string>();
        currentStates.Add("q0");

        foreach (char symbol in input)
        {
            HashSet<string> nextStates = new HashSet<string>();

            foreach (string state in currentStates)
            {
                List<string> moves = GetNextStates(state, symbol);

                foreach (string nextState in moves)
                {
                    nextStates.Add(nextState);
                }
            }

            currentStates = nextStates;
        }

        //q4 is the accepting state
        return currentStates.Contains("q4");
    }

    static List<string> GetNextStates(string state, char symbol)
    {
        List<string> result = new List<string>();

        switch (state)
        {
            case "q0":
                if (symbol == '/')
                {
                    result.Add("q1");
                }
                break;

            case "q1":
                if (symbol == '*')
                {
                    result.Add("q2");
                }
                break;

            case "q2":
                if (symbol != '*' && symbol != '/')
                {
                    //a = any character except * and /
                    result.Add("q2");
                }
                else if (symbol == '/')
                {
                    result.Add("q2");
                }
                else if (symbol == '*')
                {
                    //NFA-> two possible states
                    result.Add("q2");
                    result.Add("q3");
                }
                break;

            case "q3":
                if (symbol != '*' && symbol != '/')
                {
                    result.Add("q2");
                }
                else if (symbol == '*')
                {
                    result.Add("q3");
                }
                else if (symbol == '/')
                {
                    result.Add("q4");
                }
                break;

            case "q4":
                
                break;
        }

        return result;
    }
}