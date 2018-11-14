# xunit_to_fluent_dotnet
Small script converting Xunit asserts to FluentAssertions in .NET

Requires Python 3+

Just run the script with a path to the file containing the tests as an argument.

Do not pass the entire source file, just the lines which need converting.
An example of this is included in tests.txt

Not all Assert.* methods are included but are pretty easy to add.
