// score.gs
// Author: Jason W. Thompson
// Commentary: Being productive isn't just something that needs to happen at work. Sometimes you need to be productive 
// in other places too, like scoring a fantasy professional wrestling sheet. This extension to Google Sheets does just
// that! cerner_2^5_2018
//
// To actually try this out, there's a few things you need to do:
// 1. Create a quiz of some sort in Google Forms
// 2. Have your friends fill out their answer.
// 3. Export the results to a Google Sheet
// 4. Create a column for the points to the left of where the answers start
// 5. Create a row at row 1 where the answers will be filled in.
// 6. Click on Tool->Script Editor.
// 7. Paste this in.
// 8. In the cells for score column, just type in =score()
// Example: https://docs.google.com/spreadsheets/d/1BtsrdbzTa1vgbxnSN-nE0zIrVxLo6El94KhMfXnUhi8/edit?usp=sharing

function score() {
    // Location of cell calling the function
    var activeCell = SpreadsheetApp.getActiveRange();
    var rowIndex = activeCell.getRow();
    var colIndex = activeCell.getColumn();
    
    // Information on the ranges for the answers
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    var lastColumn = sheet.getLastColumn();
    var columnCount = lastColumn - colIndex;
    
    // Rows to compare
    var answerRow = sheet.getRange(2, colIndex + 1, 1, columnCount);
    var predictionRow = sheet.getRange(rowIndex, colIndex + 1, 1, columnCount);
    
    // Figure out score
    var score = 0;
    for (var column = 1; column <= columnCount; column++)
    {
      var answerCell = answerRow.getCell(1, column);
      var predictionCell = predictionRow.getCell(1, column);
      if (answerCell.getValue() == predictionCell.getValue()){
        score++;
      }
    }
    return score;
}
