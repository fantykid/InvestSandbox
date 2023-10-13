package UI;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
//import javafx.scene.Group;
import javafx.scene.Parent;
import javafx.scene.Scene;
//import javafx.scene.control.Label;
import javafx.stage.Stage;
public class test extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    public void start(Stage stage ) throws Exception {
        try{
            Parent root = FXMLLoader.load(getClass().getResource("SelectStock.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.show();
        }catch(Exception e){
            e.printStackTrace();
        }

    }
}
