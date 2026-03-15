from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def process(self, data: Union[int, float, List[Union[int, float]]]) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data provided.")

        items = [data] if isinstance(data, (int, float)) else data

        count = len(items)
        total = sum(items)
        avg = total / count if count > 0 else 0.0

        return f"Processed {count} numeric values, sum={total}, avg={avg:.1f}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data provided.")

        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: str) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry format.")

        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        prefix = "ALERT" if level.upper() == "ERROR" else level.upper()
        return f"[{prefix}] {level.upper()} level detected: {message}"


def main() -> None:
    _dummy_type: Optional[Any] = None
    print("=== CODE NEXUS DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
        print(num_proc.format_output(num_proc.process(num_data)))
    print()

    print("Initializing Text Processor...")
    text_proc = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f"Processing data: \"{text_data}\"")
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        print(text_proc.format_output(text_proc.process(text_data)))
    print()

    print("Initializing Log Processor...")
    log_proc = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{log_data}\"")
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        print(log_proc.format_output(log_proc.process(log_data)))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface....")

    test_cases: Dict[DataProcessor, Any] = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Code Nexus",
        LogProcessor(): "INFO: System ready"
    }

    for i, (processor, data) in enumerate(test_cases.items(), 1):
        try:
            if processor.validate(data):
                result = processor.process(data)
                print(f"Result {i}: {result}")
        except Exception as e:
            print(f"Result {i}: Processing failed - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
