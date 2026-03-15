from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.last_batch: List[Any] = []
        self.stats: Dict[str, Union[str, int, float]] = {
            "type": stream_type,
            "batch_size": 0
        }
        print(f"Stream ID: {stream_id}, Type: {stream_type}")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria is None:
                self.last_batch = [
                    item for item in data_batch if isinstance(item, str)]
            else:
                self.last_batch = [
                    item for item in data_batch
                    if isinstance(item, str) and criteria in item
                ]
        except Exception:
            self.last_batch = []
        return self.last_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        self.stats["batch_size"] = len(self.last_batch)
        return self.stats


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, "temp:")
        self.get_stats()

        try:
            temps = [float(item.split(":")[1]) for item in filtered]
            avg = sum(temps) / len(temps) if temps else 0.0
            alerts = len([t for t in temps if t > 50.0 or t < -10.0])

            self.stats["avg_temp"] = avg
            self.stats["alerts"] = alerts

            return (f"Sensor analysis: {len(filtered)} "
                    f"readings processed, avg temp: {avg:.1f}°C")
        except Exception:
            return "Sensor analysis failed."


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, ":")
        self.get_stats()

        try:
            buys = sum([int(item.split(":")[1])
                       for item in filtered if item.startswith("buy:")])
            sells = sum([int(item.split(":")[1])
                        for item in filtered if item.startswith("sell:")])
            net_flow = buys - sells

            self.stats["net_flow"] = net_flow
            self.stats["large_transactions"] = len([
                item for item in filtered if int(item.split(":")[1]) > 1000
            ])

            sign = "+" if net_flow > 0 else ""
            return (f"Transaction analysis: {len(filtered)} "
                    f"operations, net flow: {sign}{net_flow} units")
        except Exception:
            return "Transaction analysis failed."


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch)
        self.get_stats()

        try:
            errors = len(
                [item for item in filtered if "error" in item.lower()])
            self.stats["errors"] = errors

            plural = "errors" if errors != 1 else "error"
            return (f"Event analysis: {len(filtered)} events,"
                    f" {errors} {plural} detected")
        except Exception:
            return "Event analysis failed."


class StreamProcessor:
    def __init__(self) -> None:
        self.critical_alerts = 0
        self.large_transactions = 0

    def process_stream(self, stream: DataStream, batch: List[Any]) -> None:
        stream.process_batch(batch)
        stats = stream.get_stats()

        if isinstance(stream, SensorStream):
            self.critical_alerts += stats.get("alerts", 0)
            print(f"- Sensor data: {stats['batch_size']} readings processed")

        elif isinstance(stream, TransactionStream):
            self.large_transactions += stats.get("large_transactions", 0)
            print(
                f"- Transaction data: {stats['batch_size']} "
                f"operations processed")

        elif isinstance(stream, EventStream):
            print(f"- Event data: {stats['batch_size']} events processed")

    def display_filtering_report(self) -> None:
        print("Stream filtering active: High-priority data only")
        reports = []

        if self.critical_alerts > 0:
            reports.append(f"{self.critical_alerts} critical sensor alerts")
        if self.large_transactions > 0:
            reports.append(f"{self.large_transactions} large transaction")

        if reports:
            print(f"Filtered results: {', '.join(reports)}")
        else:
            print("Filtered results: None")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    s_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {s_batch}")
    print(sensor.process_batch(s_batch))
    print()

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    t_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {t_batch}")
    print(trans.process_batch(t_batch))
    print()

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    e_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {e_batch}")
    print(event.process_batch(e_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()

    mixed_batches = {
        sensor: ["temp:12", "pressure:14", "temp:85"],
        trans: ["buy:7", "sell:2500", "buy:9", "sell:9"],
        event: ["login", "error", "logout"]
    }

    print("Batch 1 Results:")
    for stream_obj, batch_data in mixed_batches.items():
        processor.process_stream(stream_obj, batch_data)

    print()
    processor.display_filtering_report()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
