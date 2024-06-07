import holded_dataflow

attributes = {
    "type": "Holded\\Product\\Domain\\Product\\Events\\ProductCreatedEvent",
    "Content-Type": "application/json",
    "targetSubscription": "Product",
    "X-Message-Stamp-Symfony\\Component\\Messenger\\Stamp\\BusNameStamp": "[{\"busName\":\"event.bus\"}]",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\CorrelationIdStamp": "[{\"id\":\"01hr71kjjn5d6zhzgjsr6eqh36\"}]",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\ContextStamp": "[{\"accountId\":\"6374be699c11acaa3108cf02\",\"userId\":null,\"platform\":null,\"correlationId\":\"01hr71kjjn5d6zhzgjsr6eqh36\"}]",
    "X-Message-Stamp-Holded\\Core\\Messaging\\Messenger\\Stamp\\TimestampStamp": "[{\"dispatchedAt\":\"2024-03-05T10:12:35+00:00\"}]",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\NewContextStamp": "[{\"actor\":{\"id\":\"65d345ca96f30a7b8f099689\",\"type\":\"api_key\"},\"accountId\":\"6374be699c11acaa3108cf02\",\"generatedBy\":\"api_key_to_context\"}]",
    "X-Message-Stamp-Holded\\Core\\Messaging\\Messenger\\Stamp\\MessageIdStamp": "[{\"id\":\"01hr71kjry3w47epk7acq7emcd\"}]",
    "X-Message-Stamp-Symfony\\Component\\Messenger\\Stamp\\HandledStamp": "[{\"result\":null,\"handlerName\":\"Holded\\\\Product\\\\Application\\\\HistoricalCost\\\\CreateHistoricalCostOnProductCreatedEventHandler::__invoke\"},{\"result\":null,\"handlerName\":\"Holded\\\\Product\\\\Application\\\\Product\\\\CounterUsage\\\\IncreaseCounterOnProductCreatedEventHandler::__invoke\"}]"
}

parsed_attributes = holded_dataflow.parse_attributes(attributes)
print(parsed_attributes["NewContextStamp"]["accountId"])
