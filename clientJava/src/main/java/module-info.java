module org.example.clientjava {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.clientjava to javafx.fxml;
    exports org.example.clientjava;
}