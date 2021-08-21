# Basic-Options_Chain-System
## What Is an Options Chain?
An **options chain**, also known as an option matrix, is a listing of all available options contracts for a given security. It shows all listed puts, calls, their expiration, strike prices, and volume and pricing information for a single underlying asset within a given maturity period. The chain will typically be categorized by expiration date and segmented by calls vs. puts. An options chain provides detailed quote and price information and should not be confused with an options series or cycle, which instead simply denotes the available strike prices or expiration dates.

I have written an abstract class "Trading System" which maintains the barebones requirements for all trading systems created as subclasses. That is, it houses a function residing in a timed infinite loop. Every instance of the TradingSystem class will assign itself the ticker and timeframe, and create a threaded infinite loop sleeping for the duration of the timeframe. This literally allows us to manage the "what" and "when" in every subclass.
I have written another class "Executer" which calls on the TradingSystem class, which implements the abstract methods and calls the options_chain() method. In the code, I have written for the Alphabet Inc.'s API which will then display the option chain on the terminal every 10 seconds.
