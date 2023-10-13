package UI;

import java.time.LocalDate;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

public class SelectStockController {
    @FXML
    private DatePicker StockHistoryData;
    @FXML
    private TextField StockNumber;
    @FXML
    private Button submitButton;

    public String getData(ActionEvent event){
        LocalDate selectedDate = StockHistoryData.getValue();
        
        return selectedDate.toString();
    }

    public String getStockNumber(ActionEvent event){
        return StockNumber.getText();
    }

    public void submit(ActionEvent event){
        System.out.println(getStockNumber(event));
        System.out.println(getData(event));
        
        
        
    }


}
