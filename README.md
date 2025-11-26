LAB 1:
Aim:- Write a program to solve “Water Jug Problem”.
Objectives:
1.	To understand state-space representation in Artificial Intelligence.
2.	To implement rule-based reasoning for problem-solving.
3.	To apply search strategies to find a sequence of valid moves.
S/W Required:- VS Code, Jupyter Notebook

Theory:
	The Water Jug Problem is a classic example of a problem-solving scenario in Artificial Intelligence. Given two jugs with different capacities and an unlimited supply of water, the objective is to measure an exact quantity using the two jugs.
Problem Definition:
We are given two jugs with capacities m liters and n liters.
The goal is to measure exactly d liters using the following allowed operations:
1.	Fill a jug completely.
2.	Empty a jug completely.
3.	Pour water from one jug into another until one is empty or the other is full.

Algorithm:
Step 1: Start from the initial state (0, 0).
Step 2: Apply the set of rules to generate new states.
Step 3: Avoid revisiting already visited states (to prevent loops).
Step 4: Continue applying rules until the goal state (x == d or y == d) is reached.
Step 5: Print the sequence of states from the initial state to the goal state.

Conclusion:- 
The Water Jug Problem demonstrates how a real-world task can be modeled and solved using Artificial Intelligence search strategies.


LAB 2:
Aim:- Implement Breadth-First and Depth-First search for solving puzzles (e.g.,8-puzzle, maze navigation).
Objectives:
1.	To understand state-space representation for problem-solving.
2.	To implement uninformed search algorithms (BFS & DFS) in Python.

S/W Required:- VS Code, Jupyter Notebook

Theory:
	I) 8-Puzzle Problem:
  Description
•	The 8-puzzle consists of a 3×3 grid containing tiles numbered 1–8 and one blank space (represented by 0).
•	A tile adjacent to the blank space can be moved into it.
•	The objective is to reach the goal configuration from a given start configuration.

  II) Maze Navigation
  Description
•	A maze is a 2D grid where:
o	0 represents an open path.
o	1 represents a wall or blocked cell.
•	The objective is to move from the start position to the goal position without crossing walls.

Problem Definition:
1.	8-Puzzle Problem
o	A sliding puzzle consisting of a 3×3 grid with tiles numbered 1–8 and one blank space.
o	The objective is to reach a goal configuration from a given initial configuration by sliding tiles into the blank space.
o	Moves allowed: Up, Down, Left, Right.

3.	Maze Navigation
o	A 2D grid maze is given where 0 represents a free cell and 1 represents a wall.
o	The task is to find a path from a start cell to a goal cell.

Algorithms:
	8 Puzzle Problem:

  Breadth-First Search (Generic):
BFS(start, goal):
    create an empty queue Q
    create a set Visited
    enqueue start into Q
    mark start as visited
    while Q is not empty:
        state = dequeue from Q
        if state == goal:
            return success
        for each neighbor of state:
            if neighbor not in Visited:
                mark neighbor as visited
                enqueue neighbor
Depth-First Search (Generic):
DFS(start, goal):
    create an empty stack S
    create a set Visited
    push start into S
    mark start as visited
    while S is not empty:
        state = pop from S
        if state == goal:
            return success
        for each neighbor of state:
            if neighbor not in Visited:
                mark neighbor as visited
                push neighbor

	Maze Navigation:

1. Initialize
•	Create a queue Q.
•	Enqueue (start, path=[start]).
•	Create an empty set Visited.
2.  While Q is not empty:
a. Dequeue the first element → (current, path).
b. If current == goal, return path (solution found).
c. If current is not in Visited:
•	Add current to Visited.
•	For each valid neighbor n of current (up, down, left, right):
o	If n is inside maze and not a wall:
	Enqueue (n, path + [n]).
3.  If queue becomes empty → No path exists.

Conclusion:- 
The implementation of the 8-Puzzle problem using Breadth-First Search (BFS) and Depth-First Search (DFS) demonstrates the working and differences between uninformed search strategies.

LAB 3:
Aim:- Solve the path-finding problem with heuristics (e.g., Manhattan or Euclidean).
Objectives:
1.	To understand the concept of heuristic search in Artificial Intelligence.
2.	To study and implement the A* search algorithm.
3.	To apply heuristic functions like Manhattan and Euclidean distance for path estimation.
4.	To find the optimal path between a start node and a goal node in a grid.

Theory:
Path-Finding Problem
Path-finding is the process of finding the shortest or most efficient route from a start point to a goal point.
It is widely used in robotics, maps, gaming, and navigation systems.
Heuristic Search
•	A heuristic is an estimate of the cost from the current node to the goal.
•	It helps guide the search algorithm towards the goal efficiently.
A Search Algorithm*
A* is a best-first search algorithm that finds the shortest path using both the actual cost so far (g(n)) and the estimated cost to the goal (h(n)).
Evaluation Function:
f(n)=g(n)+h(n)f(n) = g(n) + h(n)f(n)=g(n)+h(n) 
Where:
•	g(n)g(n)g(n): Cost from the start node to current node
•	h(n)h(n)h(n): Heuristic estimate from current node to goal
•	f(n)f(n)f(n): Total estimated cost
Algorithm (A)*
1.	Initialize open list (priority queue) with the start node.
2.	Initialize closed list as empty.
3.	While open list is not empty:
a. Pick the node with the lowest f(n).
b. If it is the goal node → Path found.
c. Else, expand its neighbors.
d. For each neighbor:
o	Calculate g(n), h(n), f(n).
o	If neighbor not in open/closed → add to open list.
o	If already present with higher cost → update cost.
4.	If open list becomes empty → No path exists.

Conclusion:- 
A* search algorithm efficiently finds the shortest path using heuristic guidance. Manhattan heuristic works well for grid-based movement in 4 directions while, Euclidean heuristic works better when diagonal movements are allowed. 

LAB 4
Aim:- Solve N-Queens, Sudoku, or Map Coloring using backtracking with forward checking.

Objectives:
1.	To understand the concept of Constraint Satisfaction Problems (CSPs).
2.	To implement Backtracking as a search strategy.
3.	To enhance efficiency using Forward Checking by pruning the search space.
4.	To solve real-world CSP problems like N-Queens, Sudoku, and Map Coloring.



Theory:
Constraint Satisfaction Problem (CSP):
A CSP is defined by:
•	Variables – elements to be assigned (e.g., queens in N-Queens, cells in Sudoku).
•	Domains – possible values for each variable (e.g., row/column positions, numbers 1–9).
•	Constraints – rules restricting assignments (e.g., no two queens attack each other, no repeated numbers in Sudoku row).
Backtracking:
Backtracking is a depth-first search strategy where:
•	Assign a value to a variable.
•	If constraints are satisfied, move to the next variable.
•	If conflict arises, backtrack (undo and try another value).
Forward Checking:
Forward Checking improves Backtracking by:
•	Looking ahead after each assignment.
•	Removing inconsistent values from the domains of unassigned variables.
•	Preventing dead ends early.

Algorithm (General Backtracking with Forward Checking):
Backtracking_FC(variables, domains, constraints):
    if all variables assigned:
        return solution
    select an unassigned variable X
    for each value v in domain(X):
        if consistent(X, v, constraints):
            assign X = v
            forward_check(X, v, domains)
            result = Backtracking_FC(variables, domains, constraints)
            if result != failure:
                return result
            undo assignment and restore domains
    return failure

Conclusion:- 
Backtracking successfully solves CSPs but may explore large search spaces.  Forward Checking reduces unnecessary exploration by pruning domains. 




LAB 5
Aim:- Implement 2-player game like Tic-Tac-Toe or Connect 4 using Minimax..
Objectives:
1.	To understand the working of the Minimax algorithm in decision-making.
2.	To implement a zero-sum two-player game where one player maximizes and the other minimizes the outcome.
3.	To design a Python program for Tic-Tac-Toe where the computer plays optimally.
4.	To demonstrate the concept of adversarial search in Artificial Intelligence.


S/W Required:- VS Code, Jupyter Notebook

Theory:
Two-Player Games
•	In a two-player zero-sum game, one player’s gain is another player’s loss.
•	Example: Tic-Tac-Toe, Chess, Connect-4.
Minimax Algorithm
The Minimax algorithm is a decision-making strategy used in adversarial search.
•	MAX player → tries to maximize score (Computer).
•	MIN player → tries to minimize score (Human opponent).
•	Game tree is explored until a terminal state (win, lose, draw).
•	Values are propagated back up the tree:
o	MAX chooses the maximum value.
o	MIN chooses the minimum value.
Tic-Tac-Toe as CSP
•	Variables: 9 cells of the board.
•	Domains: {X, O, Empty}.
•	Constraints: 3 in a row/column/diagonal wins.

Algorithm (Minimax for Tic-Tac-Toe):
function minimax(board, depth, isMaximizing):
    if terminal(board):
        return score(board)
    if isMaximizing:
        best = -∞
        for each possible move:
            make move
            value = minimax(new_board, depth+1, False)
            undo move
            best = max(best, value)
        return best
    else:
        best = +∞
        for each possible move:
            make move
            value = minimax(new_board, depth+1, True)
            undo move
            best = min(best, value)
        return best

Conclusion:- 
The Minimax algorithm ensures the computer plays optimally. In Tic-Tac-Toe, Minimax guarantees either a win or draw for the computer (never loses). 










LAB 6
Aim:  To encode a knowledge base and evaluate queries using the Truth Table and Resolution Method.
Objectives:
1.	To understand how facts and rules can be encoded in propositional or first-order logic.
2.	To evaluate queries using the truth table method for propositional logic.
3.	To apply the resolution method to infer knowledge or establish inconsistency.
4.	To implement Python programs that can automate these reasoning techniques.
5.	To demonstrate logical inference and reasoning in automated expert systems.


S/W Required:- VS Code, Jupyter Notebook

Theory:
Knowledge Representation in AI
•	A knowledge base (KB) consists of facts and rules, often represented using propositional or first-order logic.
•	Queries on the KB involve checking if a statement (proposition) can be logically derived, given the base facts/rules.
Truth Table Method
•	Generate all possible truth assignments for the variables involved.
•	Evaluate whether the query is always true whenever the premises are true.
Resolution Method
•	A rule of inference leading to refutation proofs.
•	For propositional logic, converts statements into clauses (CNF).
•	Inference proceeds by resolving pairs of clauses to deduce new information or a contradiction.

(A) Truth Table Entailment Algorithm
1.	Input: Knowledge Base (KB) as a list of propositional logic statements; Query as a propositional statement.
2.	Identify: All propositional variables in KB and Query.
3.	Generate: All possible truth assignments (combinations) for the variables.
4.	For each assignment:
•	Evaluate KB: Check if the assignment makes all KB statements true.
•	If KB is true under assignment and Query is false:
•	Entailment does not hold. Stop.
5.	If no such world exists (KB true & Query false), KB entails the Query.

(B) Resolution Algorithm
1.	Input: KB and Query in propositional logic.
2.	Convert: All sentences in KB and the negation of Query into Conjunctive Normal Form (CNF).
3.	List: All resulting clauses.
4.	Repeat:
•	Pick two clauses with complementary literals (p and ¬p).
•	Resolve them to derive a new clause.
•	If the empty clause is found:
•	Entailment is proved (KB ⊨ Query), STOP.
•	If no new clauses can be added, STOP; KB does not entail Query.

Conclusion: 

Truth table method checks all possible models; KB entails the query if it’s true in all cases. Resolution uses inferencing to derive contradictions, confirming entailment. Logical reasoning enables expert systems to answer queries based on encoded knowledge.












LAB 7
Aim:  To write a program that calculates Certainty Factors for reasoning under uncertainty.
  Objectives:
	To understand the concept of uncertainty in expert systems and AI reasoning.
	To learn how Certainty Factors (CF) are used to represent degrees of belief in uncertain knowledge.
	To implement the certainty factor model for combining evidence from multiple rules.
	To design a Python program that calculates combined certainty factors for rule-based inference.
	To demonstrate how expert systems handle uncertain or incomplete information

Theory:
Uncertainty in AI
	Real-world knowledge is often uncertain or incomplete.
	Expert systems need methods to handle degrees of belief or confidence.
Certainty Factors (CF)
	Certainty Factor is a numerical value between -1 and +1 that represents the confidence in a statement.
	CF = +1: Definitely true
	CF = 0: Unknown
	CF = -1: Definitely false
Certainty Factor Formula
For a rule: IF Evidence THEN Hypothesis [CF]
	CF(H,E)CF(H,E): Certainty factor of hypothesis H given evidence E
Combining Certainty Factors
When multiple rules lead to the same hypothesis with different certainty factors:
For CF1 and CF2 (both positive):
CFcombined= CF1 + CF2 − (CF1 × CF2) 
For CF1 and CF2 (both negative):
CFcombined= CF1 + CF2 + (CF1 × CF2)
For CF1 and CF2 (opposite signs):
CFcombined=(CF1+CF2)/(1 - min (|CF1|,|CF2|))

Algorithm
1.	Input: List of certainty factors from multiple rules for the same hypothesis.
2.	Initialize: Set CF_combined = CF1 (first certainty factor).
3.	For each subsequent CF:
•	Check if both are positive, both negative, or opposite signs.
•	Apply the appropriate combining formula.
•	Update CF_combined.
4.	Output: Final combined certainty factor.

Conclusion: 

•	Certainty factors provide a simple method to handle uncertainty in rule-based expert systems.
•	Multiple pieces of evidence can be combined systematically using CF combination formulas.
•	The final CF value indicates the overall confidence in a hypothesis based on accumulated evidence.
•	This approach is widely used in medical diagnosis, fault detection, and decision support systems.








LAB 8
Aim:  To implement Bayes’ Theorem for computing posterior probabilities based on given evidence.
  Objectives:
	To understand Bayesian reasoning and probabilistic inference in AI.
	To apply Bayes Theorem for updating beliefs based on new evidence.
	To calculate posterior probability given prior probability and likelihood.
	To implement a Python program that uses Bayes Theorem for practical decision-making.
	To demonstrate how Bayesian inference is used in medical diagnosis, spam filtering, and other AI applications.

Theory:
Probability and Bayes Theorem
Bayes Theorem provides a mathematical framework for updating our belief in hypothesis given new evidence.
Formula
P(H|E) = (P(E|H) * P(H))/(P(E))
Where:
	P(H∣E): Posterior probability – probability of hypothesis H given evidence E
	P(E∣H): Likelihood – probability of observing evidence E if hypothesis H is true
	P(H): Prior probability – initial belief in hypothesis H before observing evidence
	P(E): Total probability of evidence – marginal probability of observing E
Total Probability of Evidence
P(E)= P(E|H) * P(H)+P(E|¬H) * P(¬H)

Algorithm
	Input: Prior probability P(H), likelihood P(E|H), and probability of evidence P(E|¬H).
	Calculate: Total probability of evidence using the law of total probability.
	Apply: Bayes Theorem to compute posterior probability P(H|E).
	Output: Posterior probability value and interpretation.

Conclusion: 

•	Bayes Theorem provides a principled way to update beliefs in light of new evidence.
•	Posterior probability depends on both the prior belief and the likelihood of the observed evidence.
•	The theorem demonstrates the importance of considering base rates (prior probability) when making inferences.
•	Bayesian inference is fundamental to many AI applications including medical diagnosis, spam filtering, recommendation systems, and machine learning.







LAB 9
Aim:  To design and implement IF–THEN rule-based Expert Systems, such as a medical diagnosis system.
  Objectives:
1.	To understand the architecture and functioning of rule-based expert systems.
2.	To design and implement IF-THEN rules for knowledge representation.
3.	To develop an inference engine that processes rules and facts.
4.	To create a practical medical diagnosis expert system using rules.
5.	To demonstrate forward chaining methodology in expert systems.

S/W Required:- VS Code, Jupyter Notebook

Theory:
Expert Systems
•	Expert Systems capture human expertise in the form of rules and facts.
•	They use an inference engine to derive conclusions from knowledge bases.
•	Typical components include:
•	Knowledge Base: Facts and IF-THEN rules
•	Inference Engine: Processes rules to derive new facts
•	User Interface: Interacts with the user
•	Explanation System: Provides reasoning steps
Rule Structure
IF-THEN Rule Format:
IF (condition1 AND condition2 AND ... conditionN) THEN (conclusion)
Forward Chaining
•	Starts with known facts and applies rules to derive new facts.
•	Continues until no new facts can be derived or a goal is reached.
•	Data-driven approach: Bottom-up reasoning from evidence to conclusion.

Algorithm
1.	Initialize: Load the knowledge base (facts and rules).
2.	Add Initial Facts: Add known patient symptoms.
3.	Repeat Until No New Facts Derived:
•	For each rule in the knowledge base:
•	Check if all conditions in the IF part are satisfied by current facts.
•	If yes, add the conclusion (THEN part) to the facts.
4.	Output: All derived facts (diagnoses).

======================================================================
Conclusion: 

•	Rule-based expert systems use IF-THEN rules to capture domain knowledge.
•	Forward chaining is a practical approach for automated reasoning from facts to conclusions.
•	Expert systems can handle complex decision-making in specialized domains like medicine, finance, and manufacturing.
•	The system can be extended with more rules, certainty factors, and explanations to handle more complex scenarios.






LAB 10
Aim:  To simulate a Fuzzy Logic Controller (e.g., for fan speed or temperature control) using appropriate fuzzy rules and membership functions.
  Objectives:
	To understand fuzzy logic and fuzzy sets as an approach to handle uncertainty and imprecision.
	To learn how membership functions represent fuzzy concepts (e.g., "cold," "warm," "hot").
	To design and implement fuzzy inference systems (FIS) for decision-making.
	To create a practical fuzzy controller for automated systems like temperature control or fan speed regulation.
	To demonstrate how fuzzy logic enables intuitive reasoning similar to human thought.

Theory:
Fuzzy Logic Basics
	Classical Logic: Truth values are strictly 0 (False) or 1 (True).
	Fuzzy Logic: Truth values are continuous in the range, representing degrees of truth.
Fuzzy Sets and Membership Functions
	A fuzzy set describes a linguistic variable (e.g., "temperature").
	Membership function μ(x)μ(x) maps values to degrees of membership.
Common Membership Functions
	Triangular: μ(x)= max(0, min ( ((x-a))/((b-a)),((c-x))/((c-b))  ) )
	Trapezoidal: Similar to triangular with a flat top.
	Gaussian: μ(x)=e^(- ((x-c)^2)/(2a^2 ))
Fuzzy Inference System
	Fuzzification: Convert crisp inputs to fuzzy values using membership functions.
	Rule Evaluation: Apply fuzzy IF-THEN rules.
	Aggregation: Combine outputs from multiple rules.
	Defuzzification: Convert fuzzy output back to crisp value (e.g., Center of Mass).

Algorithm: Fuzzy Controller
	Input: Crisp values for temperature and humidity.
	Fuzzification: Calculate membership values for each fuzzy set.
	Rule Firing: Evaluate all fuzzy rules and determine their strength.
	Aggregation: Combine rule outputs.
	Defuzzification: Compute crisp output (fan speed).
	Output: Crisp fan speed value.

Conclusion: 

•	Fuzzy logic provides a powerful framework for handling imprecise and uncertain information.
•	Fuzzy controllers mimic human decision-making by using linguistic variables and rules.
•	The system smoothly transitions between states (unlike crisp logic) making it ideal for control applications.
•	Applications include air conditioning, washing machines, elevators, automotive systems, and robotic control.


