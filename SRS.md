# 1. Introduction

## 1.1 Purpose
The purpose of this document is to describe the system requirements for the writing helper application.

## 1.2 Intended Audience*
Me

## 1.3 Intended Use
This document will inform the roadmap of this project.

## 1.4 Scope
The writing prompt app is a place to generate writing prompts and write down responses to them.  Users can simply generate promtps and save them if they have logged in, or they can write responses to the prompts directly within the app.  They can then send their writing to themselves in an email.  Prompts will be generated using the chatgpt api or the deep ai api.
Stretch goal: add optional write-or-die style timer on writing space.


## 1.5 Definitions and Acronyms
Write-or-die: https://v2.writeordie.com/
ChatGPT: https://chat.openai.com/chat
DeepAI: https://deepai.org/machine-learning-model/text2img

# 2. Overall Description

## 2.1 User Needs
Sometimes writers get stuck when trying to figure out where to go next in their novels, or where to even get a starting point for a story.

## 2.2 Assumptions and Dependencies
- Assuming that ChatGPT generates prompts that writers will want to use.
- Assuming that ChatGPT will continue to support the Python API
- Assuming that DeepAI generates image prompts that writers will want to use.
- Assuming that DeepAI will continue to support the Python API

# 3. System Features and Requirements

## 3.1 Functional Requirements
- Login & signup
  - Confirmation through email
- Generate text and image prompts through APIs
- Save prompts per user
- Save text written by user per prompts
- Send text of prompt response to users emails

## 3.2 External Interface Requirements
[UI Mocks Page 1](https://github.com/bzamansky/GSU-Project-Work/blob/main/main-project/mocks_page1.pdf?raw=true)
[UI Mocks Page 2](https://github.com/bzamansky/GSU-Project-Work/blob/main/main-project/mocks_page2.pdf?raw=true)


## 3.3 System Requirements*
N/A

## 3.4 Nonfunctional Requirements
