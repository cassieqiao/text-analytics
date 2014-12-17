library(topicmodels)
library(tm)
library(wordcloud)
library(SnowballC)
library(slam)
library(reshape2)
library(ggplot2)
library(lsa)
doc.corpus  <-Corpus(DirSource("C:\\Users\\Cassie\\Google Drive\\MSiA\\Fall 2014\\MSiA 490\\hw\\characters"))
doc.corpus <- tm_map(doc.corpus, content_transformer(tolower))
doc.corpus <- tm_map(doc.corpus, removePunctuation)
doc.corpus <- tm_map(doc.corpus, removeNumbers)
doc.corpus <- tm_map(doc.corpus, removeWords, stopwords("english"))
doc.corpus <- tm_map(doc.corpus, stripWhitespace)
inspect(doc.corpus)
TDM <- TermDocumentMatrix(doc.corpus)
DTM <- DocumentTermMatrix(doc.corpus)
TDM.common = removeSparseTerms(TDM, 0.3)
TDM.dense <- as.matrix(TDM.common)
TDM.dense = melt(TDM.dense, value.name = "count")
ggplot(TDM.dense, aes(x = Docs, y = Terms, fill = log10(count))) +
       geom_tile(colour = "white") +
       scale_fill_gradient(high="#FF0000" , low="#FFFFFF")+
       ylab("") +
       theme(panel.background = element_blank()) +
       theme(axis.text.x = element_blank(), axis.ticks.x = element_blank())

m = as.matrix(DTM);
v = sort(colSums(m), decreasing=TRUE);
myNames = names(v);
k = which(names(v)=="miners");
myNames[k] = "mining";
d = data.frame(word=myNames, freq=v);
wordcloud(d$word, colors=c(3,4), random.color=FALSE, d$freq, min.freq=10);

k = 3;
SEED = 1234;
my_TM =
  list(VEM = LDA(DTM, k = k, control = list(seed = SEED)),
       VEM_fixed = LDA(DTM, k = k,
                       control = list(estimate.alpha = FALSE, seed = SEED)),
       Gibbs = LDA(DTM, k = k, method = "Gibbs",
                   control = list(seed = SEED, burnin = 1000,
                                  thin = 100, iter = 1000)),
       CTM = CTM(DTM, k = k,
                 control = list(seed = SEED,
                                var = list(tol = 10^-4), em = list(tol = 10^-3))));

Topic = topics(my_TM[["VEM"]], 1);

#top 5 terms for each topic in LDA
Terms = terms(my_TM[["VEM"]], 5);
Terms;

(my_topics =
   topics(my_TM[["VEM"]]));

most_frequent = which.max(tabulate(my_topics));

terms(my_TM[["VEM"]], 10)[, most_frequent];

# LSA
lsaSpace <- lsa(TDM)  # create LSA space
dist.mat.lsa <- dist(t(as.textmatrix(lsaSpace)))  # compute distance matrix
dist.mat.lsa  # check distance mantrix

fit <- cmdscale(dist.mat.lsa, eig = TRUE, k = 2)
points <- data.frame(x = fit$points[, 1], y = fit$points[, 2])
ggplot(points, aes(x = x, y = y)) + geom_point(data = points) + geom_text(data = points, aes(x = x, y = y - 0.2, label = c("clov","hamm","monologue","nagg","nell")))

