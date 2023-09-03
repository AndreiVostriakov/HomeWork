package Homework.Java.Homework.Task2;

public class Taskone {
    public static void main(String[] args) {
        String QUERY = "select * from students where ";
        String PARAMS = "{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"}";
        StringBuilder sb = new StringBuilder();

        sb = answer(QUERY, PARAMS);
        System.out.println(sb);
    }

    public static StringBuilder answer(String QUERY, String PARAMS) {
        PARAMS = PARAMS.replace("}", "").replace("{", "");

        String[] paramsArray = PARAMS.split(",");
        StringBuilder sb = new StringBuilder();
        sb.append(QUERY);

        for (int i = 0; i < paramsArray.length; i++) {
            String[] blockArray = paramsArray[i].split(":");
            for (int j = 0; j < blockArray.length; j++) {
                if (!paramsArray[i].contains("null")) {
                    blockArray[j] = blockArray[j].replace(" ", "");
                    if (i == 0) {
                        if (j == 0) {
                            blockArray[j] = blockArray[j].replace("\"", "");
                            sb.append(blockArray[j] + "=");
                        }
                        else {
                            blockArray[j] = blockArray[j].replace("\"", "\'");
                            sb.append(blockArray[j]);
                        }
                    }
                    else {
                        if (j == 0) {
                            blockArray[j] = blockArray[j].replace("\"", "");
                            blockArray[j] = " and " + blockArray[j];
                            sb.append(blockArray[j] + "=");
                        } else {
                            blockArray[j] = blockArray[j].replace("\"", "\'");
                            sb.append(blockArray[j]);
                        }
                    }
                }

            }
        }
        return sb;
    }
}






// class Answer {  
//     public static StringBuilder answer(String QUERY, String PARAMS){
//         String paramsNew = PARAMS.replace('{',' ').replace('}', ' ');
//         String[] params = paramsNew.split(",");
//         StringBuilder stringBuilder = new StringBuilder(QUERY);

//         for (int i = 0; i < params.length; i++){
//             String[] elements = params[i].replace('"', ' ').split(":");
//             if(!"null".equals(elements[1].trim())){       
//               stringBuilder.append(elements[0].trim()).append("=").append("'").append(elements[1].trim()).append("'");
//                 if (i < params.length - 2) stringBuilder.append(" and ");
//             }
//         }
//         return stringBuilder;
//     }
// }


// public class Printer{ 
//     public static void main(String[] args) { 
//       String QUERY = "";
//       String PARAMS = "";

//       if (args.length == 0) {
//         QUERY = "select * from students where ";
//         PARAMS = "{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"} ";
//       }
//       else{
//         QUERY = args[0];
//         PARAMS = args[1];
//       }     

//       Answer ans = new Answer();      
//       System.out.println(ans.answer(QUERY, PARAMS));
//     }
// }