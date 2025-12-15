# Vietnamese-End-to-end-Speech-Summarization
End-to-end Vietnamese Speech Summarization encoder-decoder model using Wav2Vec and T5. 

library_name: peft
base_model: huypd1508/finetuneadapter
tags:
- base_model:adapter:huypd1508/finetuneadapter
- lora
- transformers
metrics:
- rouge
model-index:
- name: w2v_t5_lora
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# w2v_t5_lora


It achieves the following results on the evaluation set:
- Loss: 2.3208
- Rouge1: 43.3573
- Rouge2: 13.8722
- Rougel: 25.8333
- Rougelsum: 25.8490

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 2
- optimizer: Use adamw_torch_fused with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 15001

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:------:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 11.9595       | 0.7015 | 3000  | 3.0937          | 35.4759 | 9.1416  | 21.8019 | 21.8007   |
| 5.5185        | 1.4029 | 6000  | 2.5475          | 40.4427 | 10.9317 | 24.2029 | 24.2018   |
| 5.0638        | 2.1043 | 9000  | 2.4144          | 34.2131 | 10.4147 | 20.5299 | 20.5693   |
| 4.9475        | 2.8058 | 12000 | 2.3583          | 45.0217 | 13.6649 | 25.9482 | 25.9543   |
| 4.7424        | 3.5072 | 15000 | 2.3208          | 43.3573 | 13.8722 | 25.8333 | 25.8490   |


### Framework versions

- PEFT 0.18.0
- Transformers 4.57.3
- Pytorch 2.9.1+cu128
- Datasets 4.4.1
- Tokenizers 0.22.1
