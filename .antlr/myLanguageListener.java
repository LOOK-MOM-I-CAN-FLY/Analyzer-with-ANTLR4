// Generated from /Users/sindi_hall/Desktop/PROGRAMMING/6_lab_ANTLR4/myLanguage.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link myLanguageParser}.
 */
public interface myLanguageListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link myLanguageParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(myLanguageParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link myLanguageParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(myLanguageParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStat(myLanguageParser.IfStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStat(myLanguageParser.IfStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfElseStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfElseStat(myLanguageParser.IfElseStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfElseStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfElseStat(myLanguageParser.IfElseStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrintStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(myLanguageParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrintStat}
	 * labeled alternative in {@link myLanguageParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(myLanguageParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LessCond}
	 * labeled alternative in {@link myLanguageParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterLessCond(myLanguageParser.LessCondContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LessCond}
	 * labeled alternative in {@link myLanguageParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitLessCond(myLanguageParser.LessCondContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EqualCond}
	 * labeled alternative in {@link myLanguageParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterEqualCond(myLanguageParser.EqualCondContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EqualCond}
	 * labeled alternative in {@link myLanguageParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitEqualCond(myLanguageParser.EqualCondContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IntExpr}
	 * labeled alternative in {@link myLanguageParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIntExpr(myLanguageParser.IntExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IntExpr}
	 * labeled alternative in {@link myLanguageParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIntExpr(myLanguageParser.IntExprContext ctx);
}