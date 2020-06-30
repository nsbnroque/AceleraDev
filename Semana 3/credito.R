library(dplyr)
library(jsonlite)

data <- read.csv("~/codenation/coestatistica-1/desafio1.csv")

#Verificando os dados
summary(data)

#Checando se existem NAs
any(is.na(data))

#Criando a função moda

Mode <- function(x) {
   ux <- unique(x)
   ux[which.max(tabulate(match(x, ux)))]
}

#Sumarizando os dados

pontuacao_credito <- data %>% group_by(estado_residencia) %>% summarize(moda = Mode(pontuacao_credito), mediana = median(pontuacao_credito), media = mean(pontuacao_credito), desvio_padrao = sd(pontuacao_credito))

#Salvando como JSON

write_json(pontuacao_credito, "pontuacao_credito.json")
