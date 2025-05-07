import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset

# Load the JSON file
with open('prompt_examples.json', 'r') as file:
    data = json.load(file)

# Create a dataset
dataset = Dataset.from_dict({
    'input': [item['input'] for item in data],
    'output': [item['output'] for item in data]
})

# Initialize the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-base")
model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-base")

# Tokenize the dataset
def tokenize_function(examples):
    inputs = tokenizer(examples['input'], padding="max_length", truncation=True, max_length=128)
    outputs = tokenizer(examples['output'], padding="max_length", truncation=True, max_length=150)
    inputs['labels'] = outputs['input_ids']
    return inputs

# Apply tokenization
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",            # Output directory for model checkpoints
    num_train_epochs=3,                # Number of epochs to train
    per_device_train_batch_size=8,     # Batch size
    per_device_eval_batch_size=8,      # Evaluation batch size
    warmup_steps=500,                  # Warmup steps
    weight_decay=0.01,                 # Weight decay
    logging_dir="./logs",              # Directory for logging
    logging_steps=10,                  # Log every 10 steps
    do_train=True,                     # Enable training
    do_eval=False                      # Disable evaluation (optional)
)

# Initialize the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine_tuned_t5')
tokenizer.save_pretrained('./fine_tuned_t5')
