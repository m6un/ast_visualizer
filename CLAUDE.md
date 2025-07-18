# AST Visualizer - Tree Learning Project

## Project Overview
This project is designed to teach tree data structures and algorithms through building an Abstract Syntax Tree (AST) parser and visualizer from scratch in Python.

## Learning Objectives
- Master tree data structures and algorithms
- Understand how parsers convert code into tree representations
- Learn recursive descent parsing techniques
- Build a complete language parser with visualization

## Phase 1: Tree Fundamentals

### 1.1 Basic Tree Node Structure
- **Node class design**: `value`, `children[]`, `parent` references
- **Tree properties**: height, depth, leaf detection
- **Memory management**: Python's garbage collection with trees
- **Node types**: differentiate between internal nodes and leaves

### 1.2 Tree Traversal Algorithms (Core Learning)
- **Pre-order traversal**: visit root → left → right (perfect for AST evaluation)
- **In-order traversal**: left → root → right (useful for expression printing)
- **Post-order traversal**: left → right → root (needed for cleanup/destruction)
- **Level-order (BFS)**: breadth-first using queue (good for tree printing)
- **Recursive vs iterative**: implement both approaches, understand call stack

### 1.3 Tree Operations
- **Insertion**: how to add nodes while maintaining tree structure
- **Deletion**: handle node removal and child re-parenting
- **Search**: find nodes by value or type
- **Tree comparison**: check if two trees are identical

### 1.4 Tree Visualization Foundations
- **Rich library**: pretty-print trees with Unicode characters
- **Custom `__str__` methods**: readable tree representation
- **Tree layout algorithms**: how to position nodes for visual clarity

## Phase 2: Tokenizer/Lexer (Language Recognition)

### 2.1 Token Theory
- **What are tokens**: smallest meaningful units (keywords, operators, literals)
- **Token types**: NUMBER, STRING, IDENTIFIER, OPERATOR, KEYWORD, EOF
- **Token attributes**: value, type, line number, column position
- **Lookahead**: peek at next characters without consuming

### 2.2 Lexer Implementation
- **Character stream processing**: iterate through source code character by character
- **State machine**: track current lexing state (in string, in number, in identifier)
- **Pattern recognition**: regex vs hand-written character matching
- **Error handling**: invalid characters, unterminated strings

### 2.3 Specific Token Handling
- **Numbers**: integers, floats, scientific notation, hex/binary
- **Strings**: escape sequences, multi-line strings, different quote types
- **Identifiers**: variable names, function names, keyword detection
- **Operators**: single char (+, -) vs multi-char (==, !=, <=)
- **Whitespace**: skip spaces/tabs, handle newlines as statement terminators
- **Comments**: single-line (//) and multi-line (/* */) comment handling

### 2.4 Advanced Lexer Features
- **Line/column tracking**: for error reporting
- **Lexer modes**: string interpolation, regex literals
- **Token buffering**: support for parser lookahead

## Phase 3: Core Parser Engine (The Heart)

### 3.1 AST Node Design
- **Base AST node class**: common properties (type, children, location)
- **Expression nodes**: BinaryOp, UnaryOp, Literal, Identifier
- **Statement nodes**: Assignment, If, While, Function
- **Visitor pattern**: separate tree traversal from node-specific logic

### 3.2 Grammar Definition
- **Context-free grammar**: formal rules for language syntax
- **EBNF notation**: extended Backus-Naur form for grammar specification
- **Production rules**: how to generate valid sentences
- **Operator precedence**: mathematical order of operations
- **Associativity**: left-to-right vs right-to-left evaluation

### 3.3 Recursive Descent Parser
- **One function per grammar rule**: `parse_expression()`, `parse_statement()`
- **Mutual recursion**: functions calling each other based on grammar
- **Backtracking**: try different parsing paths when one fails
- **Error recovery**: continue parsing after encountering errors

### 3.4 Parsing Algorithms
- **Expression parsing**: handle operator precedence correctly
- **Statement parsing**: sequence of statements, block structures
- **Recursive structures**: nested expressions, function calls
- **Lookahead**: peek at tokens to decide parsing direction

### 3.5 Error Handling
- **Syntax error detection**: unexpected tokens, missing operators
- **Error messages**: clear, helpful messages with line numbers
- **Error recovery**: synchronization points to continue parsing
- **Panic mode**: skip tokens until reaching safe recovery point

## Phase 4: Advanced Features (Real-world Complexity)

### 4.1 Operator Precedence Parser
- **Precedence climbing**: elegant algorithm for expression parsing
- **Operator tables**: precedence and associativity mappings
- **Unary operators**: prefix (-x) and postfix (x++)
- **Ternary operator**: conditional expressions (a ? b : c)

### 4.2 Variable System
- **Symbol table**: track variable declarations and scopes
- **Scope management**: nested scopes, variable shadowing
- **Type checking**: basic type inference and validation
- **Assignment vs equality**: distinguish = from ==

### 4.3 Control Flow Structures
- **If statements**: condition parsing, then/else branches
- **Loops**: while, for, do-while with break/continue
- **Block statements**: grouped statements with proper scoping
- **Nested structures**: if inside loops, loops inside functions

### 4.4 Function System
- **Function declarations**: name, parameters, return type
- **Function calls**: argument parsing, parameter matching
- **Return statements**: value expressions, early returns
- **Local variables**: function scope, parameter scope

### 4.5 Advanced Data Types
- **Arrays**: indexing, multi-dimensional arrays
- **Objects**: property access, method calls
- **String operations**: concatenation, interpolation

## Phase 5: Visualization & Testing (Making It Real)

### 5.1 Tree Visualization
- **ASCII art trees**: text-based tree display
- **Graphviz integration**: generate DOT files for publication-quality diagrams
- **Interactive visualization**: click nodes to expand/collapse
- **Syntax highlighting**: color-code different node types

### 5.2 AST Interpretation
- **Tree walking interpreter**: execute AST directly
- **Environment management**: variable storage and lookup
- **Built-in functions**: print, input, mathematical operations
- **Runtime error handling**: division by zero, undefined variables

### 5.3 Advanced Visualizations
- **Step-by-step parsing**: show parser state at each step
- **Token stream display**: visualize lexer output
- **Parse tree vs AST**: show difference between concrete and abstract syntax
- **Animation**: show tree construction in real-time

### 5.4 Testing Framework
- **Unit tests**: test individual parser components
- **Integration tests**: end-to-end parsing scenarios
- **Error testing**: verify proper error handling
- **Performance testing**: large file parsing benchmarks

### 5.5 Interactive REPL
- **Read-Eval-Print Loop**: interactive parser testing
- **Command system**: special commands for debugging
- **History**: save and recall previous inputs
- **Auto-completion**: suggest keywords and functions

## Project Structure
```
ast_visualizer/
├── tree_fundamentals.py    # Phase 1: Basic tree implementation
├── lexer.py               # Phase 2: Tokenization
├── parser.py              # Phase 3: Core parsing logic
├── ast_nodes.py           # AST node definitions
├── visualizer.py          # Tree visualization
├── interpreter.py         # AST execution engine
├── repl.py               # Interactive REPL
├── tests/                # Test suite
└── examples/             # Example code to parse
```

## Deep Learning Outcomes
- **Tree algorithms mastery**: understand how trees represent hierarchical data
- **Parsing theory**: formal language theory applications
- **Compiler design**: foundation for understanding how programming languages work
- **Pattern recognition**: recursive patterns in language design
- **Error handling**: robust software design principles

## Development Notes
- Start with simple examples and gradually increase complexity
- Test each phase thoroughly before moving to the next
- Use visualization early and often to understand tree structures
- Focus on clean, readable code that demonstrates the concepts clearly

## Learning Methodology
**This is a hands-on learning project.** The primary goal is for you to learn by doing, not by having code written for you. My role is to:
- Guide you through concepts and explain theory
- Help you understand what needs to be implemented
- Review your code and suggest improvements
- Debug issues when you get stuck
- Provide hints and direction when needed

**You should write the code yourself.** This is the only way to truly understand tree data structures, parsing algorithms, and how compilers work. I will not implement features for you unless you're completely blocked and need a specific example to understand a concept.