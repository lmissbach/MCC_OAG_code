l


ibrary(dplyr)
library(magrittr)

# Load the CSV file into a data frame
results_germany <- read.csv("C:/Users/Giulia Maria/Documents/GitHub/MCC_OAG_code/R/Results_tables/Results (2).csv")

# View the first 5 observations of the data frame
head(results_germany, 5)
library(dplyr)

unique_entries <- results_germany |>
  select(Airport.Name ) |>
  distinct() |>
  nrow()


unique_entries


  unique(IATA)

unique_entries




