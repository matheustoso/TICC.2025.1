STYLESHEET = """

Screen {
    overflow: auto;
}

#app {
    layout: vertical;
}

#textContainer {
    min-height: 6;
    background: #5C3D2E;
    padding: 1;
}

#optionsContainer {
    min-height: 5;
    max-height: 10;
    background: #5C3D2E;
    padding: 1;
}

#text {
    min-height: 10;
}

#options {
    layout: horizontal;
    width: 100%;
    content-align: center middle;
    align: center middle;
    height: 7;
}

#operation {
    height: 100%;
    background: #2D2424;
    width: 40%;
}

#algorithm {
    height: 100%;
    background: #2D2424;
    width: 40%;
}

#execute {
    margin: 1 0 0 0;
    width: 100%;
    text-align: center;
    align: center middle;
    text-style: bold;
    background: #B85C38;
}

#input {
    width: 40%;
    content-align: center middle;
}

#inputArea {
    width: 100%;
    background: #2D2424;
    height: 3;
}

#inputText{
    width: 100%;
    background: #2D2424;
}

#output {
    width: 40%;
}

#outputText {
    background: #2D2424;
}

#alphabet {
    width: 20%;
}

#randomButton {
    width: 100%;
    text-align: center;
    align: center middle;
    text-style: bold;
    background: #E0C097;
}

#buttons {
    width: 20%;
    height: 100%
}

#logContainer {
    background: #5C3D2E;
    height: 4;
    padding: 0 1 1 2;
}

#log {
    background: #2D2424;
    height: 3;
    scrollbar-size: 0 0;
}

Label {
    width: 100%;
    text-align: center;
}

"""