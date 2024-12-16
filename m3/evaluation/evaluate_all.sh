#!/bin/bash

sh evaluate.sh party complex
sh evaluate.sh party pure_semantic
sh evaluate.sh party rerank

sh evaluate.sh steal complex
sh evaluate.sh steal pure_semantic
sh evaluate.sh steal rerank

sh evaluate.sh mega complex
sh evaluate.sh mega pure_semantic
sh evaluate.sh mega rerank

sh evaluate.sh ashBattle complex
sh evaluate.sh ashBattle pure_semantic
sh evaluate.sh ashBattle rerank