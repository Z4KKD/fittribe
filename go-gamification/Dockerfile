FROM golang:1.17

WORKDIR /app

COPY go.mod ./
COPY . ./

RUN go mod tidy && go build -o main .

EXPOSE 9000

CMD ["./main"]
