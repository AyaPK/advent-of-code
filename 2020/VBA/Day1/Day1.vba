
''' Assumes the input data is in Column 1 and that Cell 1B is free to display the output

Private Sub CommandButton1_Click()
    Dim x As Long
    x = 1
    Dim item_one As Long
    Dim item_two As Long
    Dim item_three As Long
    
    Dim a As Long
    Dim b As Long
    Dim c As Long
    
    Dim out As Long
    
    For item_one = 1 To 200
        For item_two = 1 To 200
            For item_three = 1 To 200
                a = Cells(item_one, 1).Value
                b = Cells(item_two, 1).Value
                c = Cells(item_three, 1).Value
                out = (a + b + c)
                If out = 2020 Then
                    Dim final As Long
                    final = (a * b * c)
                    Cells(1, 2).Value = final
                    Exit Sub
                End If
            Next item_three
        Next item_two
    Next item_one
End Sub

